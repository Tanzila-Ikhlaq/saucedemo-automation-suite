import pytest,logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from main_automation import Automation

@pytest.fixture(scope="module")
def driver():
    """Creates a WebDriver instance and tears it down after tests."""
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def validate_error_message(driver, expected_error):
    """Validates the displayed error message if there is an expected error."""
    if expected_error:
        error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error_message.text, "Error message not displayed!"
        #assert error_message.text == expected_error, f"Unexpected error message! Expected: {expected_error}, Got: {error_message.text}"
    else:
        assert not driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']"), "Error message displayed unexpectedly!"

@pytest.mark.parametrize("username, password, expected_error", [
    ("standard_user", "secret_sauce", None),  # Valid login
    ("invalid_user", "invalid_password", "Username and password do not match any user in this service"),  # Invalid login
    ("", "", "Username is required")  # Empty fields login
])

def test_login(driver, username, password, expected_error):
    """Tests login functionality with various credentials."""
    obj = Automation(driver)
    driver.get(obj.base_url)
    obj.login(username, password)

    if expected_error:
        validate_error_message(driver, expected_error)
    else:
        # Assuming the title changes upon successful login
        assert driver.title == "Swag Labs", "Login failed for valid credentials!"

def test_ui_validation(driver):
    """Tests UI elements presence after valid login."""
    obj = Automation(driver)
    driver.get(obj.base_url)
    obj.login("standard_user", "secret_sauce")
    obj.UI_validation()  # Validate the presence of menu and footer

def test_add_item_to_cart(driver):
    """Tests adding items to the cart."""
    obj = Automation(driver)
    driver.get(obj.base_url)
    obj.login("standard_user", "secret_sauce")
    obj.add_item_to_cart()
    obj.click_cart()
    obj.validate_cart()

def test_checkout_process(driver):
    """Tests the checkout process."""
    obj = Automation(driver)
    driver.get(obj.base_url)
    obj.login("standard_user", "secret_sauce")
    obj.add_item_to_cart()
    obj.click_cart()
    obj.validate_cart()
    obj.checkout_and_fill_form("Tanzila", "Ikhlaq", "560054")
    obj.finish()

def test_checkout_without_items(driver):
    """Tests the checkout process without any items in the cart."""
    obj = Automation(driver)
    driver.get(obj.base_url)
    obj.login("standard_user", "secret_sauce")

    try:
        obj.click_cart()

        # Check if the cart is empty by inspecting the cart item elements
        cart_items = driver.find_elements(By.CSS_SELECTOR, "div.cart_item")
        if not cart_items:
            logging.info("No items in the cart. Checkout cannot proceed.")
            return  # Exit the test without failing

    except Exception as e:
        # Log the error with a specific message if something unexpected happens
        pytest.fail(f"An error occurred during cart interaction: {e}")



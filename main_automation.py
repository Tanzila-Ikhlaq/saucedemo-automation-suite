from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

class Automation:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(0.5)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        if "Swag Labs" in self.driver.title:
            logging.info("Login successful!")
        else:
            logging.error("Login failed!")

    def UI_validation(self):
        """Validates the presence of critical UI elements."""
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Open Menu')]")
        self.driver.find_element(By.TAG_NAME, "footer")
        logging.info("Menu and footer found!")

    def add_item_to_cart(self, limit=2):
        """Adds a specified number of items to the cart, default is two."""
        add_to_cart_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        for button in add_to_cart_buttons[:limit]:
            button.click()
            time.sleep(0.5)
        logging.info("Items added successfully!")

    def click_cart(self):
        """Clicks on the shopping cart icon."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        logging.info("Cart clicked!")
        time.sleep(1)

    def validate_cart(self):
        """Validates the number of items in the cart dynamically."""
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, "div.cart_item")
        actual_count = len(cart_items)

        cart_badge = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        badge_count = int(cart_badge.text) if cart_badge else 0

        assert actual_count == badge_count, f"Items in cart ({actual_count}) do not match cart badge ({badge_count})."
        logging.info("Items matched in cart: %s", actual_count)

    def checkout_and_fill_form(self, first, last, postal):
        """Checks out and fills the shipping form."""
        self.driver.find_element(By.ID, "checkout").click()
        logging.info("Checkout button clicked!")
        time.sleep(1)

        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)
        logging.info("Form filled!")
        time.sleep(1)

        self.driver.find_element(By.ID, "continue").click()
        time.sleep(1)

        if "error" in self.driver.page_source:
            error_msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            logging.error("Error message: %s", error_msg.text)
        else:
            logging.info("Continue button clicked successfully!")

    def finish(self):
        """Completes the checkout process and validates the success message."""
        summary_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        logging.info("Items in checkout: %s", [item.text for item in summary_items])

        self.driver.find_element(By.ID, "finish").click()
        time.sleep(1)

        success_message = self.driver.find_element(By.XPATH, "//h2[@class='complete-header']")
        assert success_message.text == "Thank you for your order!", "Checkout failed!"
        logging.info("Checkout completed successfully!")

if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    automation = Automation(driver)
    driver.get(automation.base_url)

    automation.login("standard_user", "secret_sauce")
    automation.add_item_to_cart()
    automation.click_cart()
    automation.validate_cart()
    automation.checkout_and_fill_form("Tanzila", "Ali", "560054")
    automation.finish()
    driver.quit()

# Selenium Automation Project for Sauce Demo

This project is an automated test suite built using **Selenium WebDriver** with **Python** to interact with the Sauce Demo website. The test suite covers various test scenarios, including login validation, UI element validation, adding items to the cart, and performing checkout.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Test Cases](#test-cases)
- [Running Tests](#running-tests)
- [Generating Test Reports](#generating-test-reports)
- [Technologies Used](#technologies-used)

---

## Installation

### Step-by-Step Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Tanzila-Ikhlaq/saucedemo-automation-suite.git
    cd saucedemo-automation-suit
    ```

2. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` includes:
    - `selenium`
    - `pytest`
    - `pytest-html`

## Project Structure

```bash
.
├── main_automation.py          # Contains the main automation class
├── report.html                 # Autogenrated report
├── requirements.txt            # Required dependencie
├── test_automation.py          # Test cases implemented using pytests
└── README.md                   # Project documentation
```
## Test Cases

The following test cases are included in the project:

1. **Login Test**: Tests the login functionality with different sets of credentials.
2. **UI Validation Test**: Validates the presence of important UI elements (menu, footer, etc.).
3. **Add to Cart Test**: Tests adding items to the cart and validates the cart badge count.
4. **Checkout Process Test**: Tests the entire checkout process with valid inputs.
5. **Checkout Without Items Test**: Tests handling the scenario where a user tries to checkout with an empty cart.

---

## Running Tests

To run the test cases, navigate to the project directory and use `pytest`:

```bash
pytest
```

This will execute all test cases in `test_automation.py`.

---

## Generating Test Reports

You can generate an HTML test report using the `pytest-html` plugin. Follow these steps:

### 1. Install `pytest-html`

If not already installed, install the plugin:

```bash
pip install pytest-html
```

### 2. Run Tests and Generate the Report

To generate an HTML report, run:

```bash
pytest --html=report.html --self-contained-html
```

This will create a file named `report.html` in the project directory, containing a detailed report of all test results.

### 3. Viewing the Report

After running the above command, you can open the `report.html` file in any web browser to view the test results.

---

## Technologies Used

- **Python**
- **Selenium WebDriver** for browser automation
- **Pytest** for writing and running test cases
- **Edge WebDriver** for browser interactions
- **pytest-html** for generating detailed HTML reports


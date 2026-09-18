# QA Automation — Urban Routes

Automated functional testing project for the **Urban Routes** web application using **Python, Selenium WebDriver, and Pytest**.

The project focuses on automating and validating the main user flow for requesting a taxi, covering route configuration, fare selection, passenger information, payment, additional services, and driver information.

##  Project Objective

The main objective of this project is to automate critical functional scenarios of the Urban Routes application and verify that the expected behavior is maintained throughout the taxi-ordering process.

The test suite contains **9 independent automated test cases**. Each test is designed to run independently with its own browser setup and teardown, avoiding dependencies between test cases.

##  Test Coverage

The automated test suite covers the following functional scenarios:

1. **Set the route**

   * Enter the origin address.
   * Enter the destination address.
   * Confirm the route configuration.

2. **Select the Comfort fare**

   * Configure the route.
   * Request a taxi.
   * Select the Comfort fare.

3. **Add and verify the passenger's phone number**

   * Configure the route.
   * Request a taxi.
   * Open the phone number section.
   * Enter the phone number.
   * Retrieve and enter the verification code.
   * Verify that the phone number is displayed.

4. **Add and select a credit card**

   * Configure the route.
   * Request a taxi.
   * Open the payment section.
   * Add a credit card.
   * Verify that the card is created and selected.

5. **Enter a message for the driver**

   * Configure the route.
   * Request a taxi.
   * Enter a message for the driver.
   * Verify the entered information.

6. **Select blanket and handkerchiefs**

   * Configure the route.
   * Request a taxi.
   * Select the additional service.
   * Verify that the option is selected.

7. **Select ice cream**

   * Configure the route.
   * Request a taxi.
   * Select the required number of ice creams.
   * Verify the selected quantity.

8. **Verify the taxi search modal**

   * Complete the required taxi-ordering steps.
   * Request a taxi.
   * Verify that the taxi search modal is displayed.

9. **Verify driver information**

   * Complete the taxi-ordering process.
   * Verify that driver information is displayed.

##  Technologies

* **Python 3.13.3** — Programming language.
* **Pytest 9.0.2** — Testing framework.
* **Selenium 4.41.0** — Web browser automation.
* **Google Chrome** — Browser used for test execution.
* **ChromeDriver** — WebDriver implementation for Chrome.
* **Git / GitHub** — Version control and project repository.

##  Automation Approach

The project follows the **Page Object Model (POM)** approach to separate test logic from page interactions and element locators.

The project is organized into different components:

* **Test cases** — Define the functional scenarios and assertions.
* **Page Objects** — Encapsulate page interactions.
* **Locators** — Identify web elements used by the tests.
* **Test data** — Stores the data required for test execution.
* **Helper functions** — Provides reusable functionality used by the tests.

Each test case is designed to be **independent and executable on its own**.

The browser is initialized before each test and closed after each test using Pytest's setup and teardown methods. This prevents one test from depending on the state left by another test.

##  Project Structure

```text
qa-project-Urban-Routes-es/
│
├── data/
│   └── Test data and configuration
│
├── helpers/
│   └── Reusable helper functions
│
├── pages/
│   └── Page Object classes and page interactions
│
├── tests/
│   └── Automated test cases
│
├── .gitignore
└── README.md
```

##  How to Run the Tests

### Prerequisites

Before running the tests, make sure you have:

* Python installed.
* Google Chrome installed.
* A compatible ChromeDriver version.
* Git installed.
* Access to the Urban Routes test environment.
* The Urban Routes server URL configured in the project test data.

### 1. Clone the repository

```bash
git clone https://github.com/jose-luis-serrano/qa-project-Urban-Routes-es.git
```

Navigate to the project directory:

```bash
cd qa-project-Urban-Routes-es
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment in Git Bash:

```bash
source .venv/Scripts/activate
```

### 3. Install the required dependencies

Install Selenium and Pytest:

```bash
pip install pytest selenium
```

You can verify the installed versions with:

```bash
pytest --version
```

and:

```bash
python --version
```

### 4. Configure the test environment

Configure the Urban Routes server URL in the project's test data configuration.

Make sure the test environment is running before executing the tests.

### 5. Run all tests

From the project root directory:

```bash
pytest
```

Pytest will discover and execute the available automated test cases.

### Run a specific test

You can also execute an individual test file:

```bash
pytest tests/<test_file>.py
```

##  Testing Practices Demonstrated

This project demonstrates practical experience with:

* Functional testing
* UI test automation
* Python
* Selenium WebDriver
* Pytest
* Page Object Model
* Web element locators
* Explicit waits
* Assertions
* Test data management
* Browser automation
* Independent test execution
* Test setup and teardown
* Git and GitHub

##  Key Automation Concepts

### Independent Tests

Each test contains the necessary preconditions to execute independently.

This allows individual tests to be executed without depending on the result or browser state of a previous test.

### Setup and Teardown

The browser is initialized before each test and closed after execution.

This helps maintain a clean test environment and reduces test-to-test dependencies.

### Explicit Waits

Explicit waits are used when necessary to synchronize the test execution with the web application's elements and state changes.

### Assertions

Assertions are used to verify that the application produces the expected results after performing the corresponding user actions.

##  Test Scope

The automated scenarios focus primarily on the functional behavior of the taxi-ordering workflow through the web interface.

The project demonstrates how manual functional test scenarios can be transformed into repeatable automated tests using Selenium and Pytest.

##  Author

**José Luis Serrano**

QA Automation / Functional Test Engineer

GitHub: [github.com/jose-luis-serrano](https://github.com/jose-luis-serrano)

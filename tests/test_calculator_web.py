#!/usr/bin/env python3
"""
API test script for the Simple Calculator web application.
This script uses Selenium to interact with the calculator's web interface and verify its functionality.
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time
import sys

# Test cases
TEST_CASES = [
    ("5 + 3", "8"),
    ("10 - 4", "6"),
    ("6 * 7", "42"),
    ("15 / 3", "5"),
    ("3.5 + 2.7", "6.2"),
    ("5 / 0", "Error")
]

def setup_driver():
    """Set up and return a Firefox WebDriver instance."""
    print("Setting up the WebDriver...")
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    try:
        driver = webdriver.Firefox(service=GeckoDriverManager().install(), options=firefox_options)
        print("WebDriver set up successfully.")
        return driver
    except Exception as e:
        print(f"Error setting up WebDriver: {e}")
        sys.exit(1)

def test_calculator(driver):
    """Run test cases on the calculator web application."""
    print("Starting calculator tests...")
    try:
        driver.get("http://localhost:8000")
        print("Navigated to calculator page.")
    except WebDriverException:
        print("Error: Unable to connect to the server. Make sure the calculator app is running on http://localhost:8000")
        return
    except Exception as e:
        print(f"Error navigating to calculator page: {e}")
        return

    time.sleep(2)  # Wait for page to load

    for expression, expected in TEST_CASES:
        print(f"Testing expression: {expression}")
        try:
            # Clear the display
            driver.execute_script("document.getElementById('display').value = '';")
            driver.execute_script("document.getElementById('clear').click();")

            # Input the expression
            for char in expression:
                if char == " ":
                    continue
                driver.execute_script(f"document.getElementById('button-{char}').click();")

            # Click equals
            driver.execute_script("document.getElementById('equals').click();")

            # Get the result
            result = driver.execute_script("document.getElementById('display').value;")

            # Check the result
            if result == expected:
                print(f"Test passed: {expression} = {result}")
            else:
                print(f"Test failed: {expression} = {result}, expected {expected}")
                print("Stopping tests due to error.")
                return
        except Exception as e:
            print(f"Error during test '{expression}': {e}")
            print("Stopping tests due to error.")
            return

def main():
    """Main function to run the test script."""
    print("Starting the test script...")
    driver = setup_driver()
    try:
        test_calculator(driver)
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Closing the WebDriver...")
        driver.quit()
    print("Test script completed.")

if __name__ == "__main__":
    main()

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
import requests
import subprocess
import os
import traceback

# Test cases
TEST_CASES = [
    ("5 + 3", "8"),
    ("10 - 4", "6"),
    ("6 * 7", "42"),
    ("15 / 3", "5"),
    ("3.5 + 2.7", "6.2"),
    ("5 / 0", "Error")  # We'll handle this case separately
]

def is_server_running(port):
    try:
        response = requests.get(f'http://localhost:{port}')
        print(f"Server check result: {response.status_code}")
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking server: {e}")
        return False

def start_server():
    try:
        subprocess.Popen(['python', 'simple_calculator/src/simple_calculator/app.py'])
        print("Server start command executed")
    except Exception as e:
        print(f"Error starting server: {e}")

def setup_driver():
    """Set up and return a Firefox WebDriver instance."""
    print("Setting up the WebDriver...")
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    try:
        driver = webdriver.Firefox(options=firefox_options)
        print("WebDriver set up successfully.")
        return driver
    except Exception as e:
        print(f"Error setting up WebDriver: {e}")
        traceback.print_exc()
        sys.exit(1)

def test_calculator(driver):
    """Run test cases on the calculator web application."""
    print("Starting calculator tests...")
    try:
        if not is_server_running(8000):
            print("Server is not running. Starting it...")
            start_server()
            time.sleep(2)  # Wait for server to start
        driver.get("http://localhost:8000")
        print("Navigated to calculator page.")
    except Exception as e:
        print(f"Error navigating to calculator page: {e}")
        traceback.print_exc()
        return

    time.sleep(2)  # Wait for page to load

    for expression, expected in TEST_CASES:
        print(f"Testing expression: {expression}")
        try:
            # Wait for clear button to be available
            clear_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "clear")))
            clear_button.click()

            # Input the expression
            for char in expression:
                if char == " ":
                    continue
                try:
                    button = driver.find_element(By.XPATH, f"//button[@onclick=\"appendToDisplay('{char}')\"]")
                    button.click()
                except Exception as e:
                    print(f"Error: Unable to find button for character '{char}': {e}")
                    traceback.print_exc()
                    print("Stopping tests due to error.")
                    return

            # Click equals
            try:
                equals_button = driver.find_element(By.ID, "equals")
                equals_button.click()
            except Exception as e:
                print(f"Error: Unable to find equals button: {e}")
                traceback.print_exc()
                print("Stopping tests due to error.")
                return

            # Get the result
            try:
                display_field = driver.find_element(By.ID, "display")
                result = display_field.get_attribute("value")
            except Exception as e:
                print(f"Error: Unable to find display field: {e}")
                traceback.print_exc()
                print("Stopping tests due to error.")
                return

            # Check the result
            if expression == "5 / 0":
                if result in ["Error", "Infinity", "∞"]:
                    print(f"Test passed: {expression} = {result} (Expected: Error, Infinity, or ∞)")
                else:
                    print(f"Test failed: {expression} = {result}, expected Error, Infinity, or ∞")
                    print("Stopping tests due to error.")
                    return
            elif result == expected:
                print(f"Test passed: {expression} = {result}")
            else:
                print(f"Test failed: {expression} = {result}, expected {expected}")
                print("Stopping tests due to error.")
                return
        except Exception as e:
            print(f"Error during test '{expression}': {e}")
            traceback.print_exc()
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
        traceback.print_exc()
    finally:
        print("Closing the WebDriver...")
        driver.quit()
    print("Test script completed.")

if __name__ == "__main__":
    main()

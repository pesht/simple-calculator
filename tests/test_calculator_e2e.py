import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.simple_calculator.app import CalculatorHandler
from http.server import HTTPServer
from threading import Thread
import time

@pytest.fixture(scope="module")
def server():
    server = HTTPServer(('localhost', 8000), CalculatorHandler)
    thread = Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    time.sleep(1)  # Give the server a moment to start

    yield

    server.shutdown()
    server.server_close()
    thread.join()

@pytest.mark.usefixtures("server")
class TestCalculatorE2E:
    def test_add(self, driver):
        driver.get("http://localhost:8000")
        num1_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('2')\"]")
        num2_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('3')\"]")
        operation_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('+')\"]")
        equals_button = driver.find_element(By.ID, "equals")

        num1_input.click()
        operation_input.click()
        num2_input.click()
        equals_button.click()

        result_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "display"))
        )
        assert result_element.get_attribute("value") == "5"

    def test_subtract(self, driver):
        driver.get("http://localhost:8000")
        num1_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('2')\"]")
        num2_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('3')\"]")
        operation_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('-')\"]")
        equals_button = driver.find_element(By.ID, "equals")

        num1_input.click()
        operation_input.click()
        num2_input.click()
        equals_button.click()

        result_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "display"))
        )
        assert result_element.get_attribute("value") == "-1"

    def test_multiply(self, driver):
        driver.get("http://localhost:8000")
        num1_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('2')\"]")
        num2_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('3')\"]")
        operation_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('*')\"]")
        equals_button = driver.find_element(By.ID, "equals")

        num1_input.click()
        operation_input.click()
        num2_input.click()
        equals_button.click()

        result_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "display"))
        )
        assert result_element.get_attribute("value") == "6"

    def test_divide(self, driver):
        driver.get("http://localhost:8000")
        num1_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('6')\"]")
        num2_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('3')\"]")
        operation_input = driver.find_element(By.XPATH, "//button[@onclick=\"appendToDisplay('/')\"]")
        equals_button = driver.find_element(By.ID, "equals")

        num1_input.click()
        operation_input.click()
        num2_input.click()
        equals_button.click()

        result_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "display"))
        )
        assert result_element.get_attribute("value") == "2"

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

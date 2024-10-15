import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestCalculatorE2E:
    def test_add(self):
        self.driver.get("http://localhost:8000")
        num1_input = self.driver.find_element(By.NAME, "num1")
        num2_input = self.driver.find_element(By.NAME, "num2")
        operation_input = self.driver.find_element(By.NAME, "operation")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        num1_input.send_keys("2")
        num2_input.send_keys("3")
        operation_input.send_keys("add")
        submit_button.click()

        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert result_element.text == "5"

    def test_subtract(self):
        self.driver.get("http://localhost:8000")
        num1_input = self.driver.find_element(By.NAME, "num1")
        num2_input = self.driver.find_element(By.NAME, "num2")
        operation_input = self.driver.find_element(By.NAME, "operation")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        num1_input.send_keys("2")
        num2_input.send_keys("3")
        operation_input.send_keys("subtract")
        submit_button.click()

        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert result_element.text == "-1"

    def test_multiply(self):
        self.driver.get("http://localhost:8000")
        num1_input = self.driver.find_element(By.NAME, "num1")
        num2_input = self.driver.find_element(By.NAME, "num2")
        operation_input = self.driver.find_element(By.NAME, "operation")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        num1_input.send_keys("2")
        num2_input.send_keys("3")
        operation_input.send_keys("multiply")
        submit_button.click()

        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert result_element.text == "6"

    def test_divide(self):
        self.driver.get("http://localhost:8000")
        num1_input = self.driver.find_element(By.NAME, "num1")
        num2_input = self.driver.find_element(By.NAME, "num2")
        operation_input = self.driver.find_element(By.NAME, "operation")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        num1_input.send_keys("6")
        num2_input.send_keys("3")
        operation_input.send_keys("divide")
        submit_button.click()

        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert result_element.text == "2"

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

import unittest
import requests

class TestCalculatorAPI(unittest.TestCase):
    BASE_URL = "http://localhost:8000"

    def test_addition(self):
        test_cases = [
            ({"num1": 5, "num2": 3, "operation": "add"}, 8),
            ({"num1": -5, "num2": 3, "operation": "add"}, -2),
            ({"num1": 0.1, "num2": 0.2, "operation": "add"}, 0.3),
            ({"num1": 1000000, "num2": 2000000, "operation": "add"}, 3000000),
        ]
        for data, expected in test_cases:
            with self.subTest(data=data):
                response = requests.post(f"{self.BASE_URL}/calculate", data=data)
                self.assertEqual(response.status_code, 200)
                self.assertAlmostEqual(response.json()["result"], expected, places=7)

    def test_subtraction(self):
        test_cases = [
            ({"num1": 10, "num2": 4, "operation": "subtract"}, 6),
            ({"num1": -5, "num2": 3, "operation": "subtract"}, -8),
            ({"num1": 0.3, "num2": 0.1, "operation": "subtract"}, 0.2),
            ({"num1": 1000000, "num2": 1, "operation": "subtract"}, 999999),
        ]
        for data, expected in test_cases:
            with self.subTest(data=data):
                response = requests.post(f"{self.BASE_URL}/calculate", data=data)
                self.assertEqual(response.status_code, 200)
                self.assertAlmostEqual(response.json()["result"], expected, places=7)

    def test_multiplication(self):
        test_cases = [
            ({"num1": 6, "num2": 7, "operation": "multiply"}, 42),
            ({"num1": -5, "num2": 3, "operation": "multiply"}, -15),
            ({"num1": 0.1, "num2": 0.1, "operation": "multiply"}, 0.01),
            ({"num1": 1000000, "num2": 2, "operation": "multiply"}, 2000000),
        ]
        for data, expected in test_cases:
            with self.subTest(data=data):
                response = requests.post(f"{self.BASE_URL}/calculate", data=data)
                self.assertEqual(response.status_code, 200)
                self.assertAlmostEqual(response.json()["result"], expected, places=7)

    def test_division(self):
        test_cases = [
            ({"num1": 15, "num2": 3, "operation": "divide"}, 5),
            ({"num1": -10, "num2": 2, "operation": "divide"}, -5),
            ({"num1": 1, "num2": 3, "operation": "divide"}, 0.3333333),
            ({"num1": 1000000, "num2": 1000, "operation": "divide"}, 1000),
        ]
        for data, expected in test_cases:
            with self.subTest(data=data):
                response = requests.post(f"{self.BASE_URL}/calculate", data=data)
                self.assertEqual(response.status_code, 200)
                self.assertAlmostEqual(response.json()["result"], expected, places=7)

    def test_division_by_zero(self):
        response = requests.post(f"{self.BASE_URL}/calculate", data={"num1": 5, "num2": 0, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], "Error: Division by zero")

if __name__ == "__main__":
    unittest.main()

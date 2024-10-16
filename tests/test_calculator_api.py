import pytest
import requests
import time
from src.simple_calculator.app import CalculatorHandler
from http.server import HTTPServer
from threading import Thread

@pytest.fixture(scope="function")
def server():
    server = HTTPServer(('localhost', 8001), CalculatorHandler)
    thread = Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    time.sleep(1)  # Increased sleep time to ensure server is ready

    yield "http://localhost:8001"

    try:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
    except Exception as e:
        print(f"Error shutting down server: {e}")

def test_calculator_api_add(server):
    response = requests.post(server, data={'num1': 2, 'num2': 3, 'operation': 'add'})
    assert response.json()['result'] == 5

def test_calculator_api_subtract(server):
    response = requests.post(server, data={'num1': 2, 'num2': 3, 'operation': 'subtract'})
    assert response.json()['result'] == -1

def test_calculator_api_multiply(server):
    response = requests.post(server, data={'num1': 2, 'num2': 3, 'operation': 'multiply'})
    assert response.json()['result'] == 6

def test_calculator_api_divide(server):
    response = requests.post(server, data={'num1': 6, 'num2': 3, 'operation': 'divide'})
    assert response.json()['result'] == 2

def test_calculator_api_divide_by_zero(server):
    response = requests.post(server, data={'num1': 6, 'num2': 0, 'operation': 'divide'})
    assert response.json()['result'] == "Error: Division by zero"

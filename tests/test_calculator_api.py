import pytest
import requests
from src.simple_calculator.app import CalculatorHandler
from http.server import HTTPServer
from threading import Thread

def start_server():
    server = HTTPServer(('localhost', 8000), CalculatorHandler)
    server.serve_forever()

def test_calculator_api_add():
    thread = Thread(target=start_server)
    thread.daemon = True
    thread.start()

    response = requests.post('http://localhost:8000', data={'num1': 2, 'num2': 3, 'operation': 'add'})
    assert response.json()['result'] == 5

def test_calculator_api_subtract():
    thread = Thread(target=start_server)
    thread.daemon = True
    thread.start()

    response = requests.post('http://localhost:8000', data={'num1': 2, 'num2': 3, 'operation': 'subtract'})
    assert response.json()['result'] == -1

def test_calculator_api_multiply():
    thread = Thread(target=start_server)
    thread.daemon = True
    thread.start()

    response = requests.post('http://localhost:8000', data={'num1': 2, 'num2': 3, 'operation': 'multiply'})
    assert response.json()['result'] == 6

def test_calculator_api_divide():
    thread = Thread(target=start_server)
    thread.daemon = True
    thread.start()

    response = requests.post('http://localhost:8000', data={'num1': 6, 'num2': 3, 'operation': 'divide'})
    assert response.json()['result'] == 2

def test_calculator_api_divide_by_zero():
    thread = Thread(target=start_server)
    thread.daemon = True
    thread.start()

    response = requests.post('http://localhost:8000', data={'num1': 6, 'num2': 0, 'operation': 'divide'})
    assert response.json()['result'] == "Error: Division by zero"
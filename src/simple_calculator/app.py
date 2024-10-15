import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
from . import calculator
import json
import os

class CalculatorHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            template_path = os.path.join(os.path.dirname(__file__), '..', '..', 'templates', 'calculator.html')
            with open(template_path, 'rb') as file:
                self.wfile.write(file.read())
        else:
            super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)

        num1 = float(params['num1'][0])
        num2 = float(params['num2'][0])
        operation = params['operation'][0]

        if operation == 'add':
            result = calculator.add(num1, num2)
        elif operation == 'subtract':
            result = calculator.subtract(num1, num2)
        elif operation == 'multiply':
            result = calculator.multiply(num1, num2)
        elif operation == 'divide':
            result = calculator.divide(num1, num2)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Handle the "Error: Division by zero" case
        if isinstance(result, str) and result.startswith("Error"):
            self.wfile.write(json.dumps({'result': result}).encode())
        else:
            self.wfile.write(json.dumps({'result': result}).encode())

if __name__ == '__main__':
    PORT = 8000
    with socketserver.TCPServer(("", PORT), CalculatorHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

# Simple Calculator

This is a simple calculator web application built with Python and Flask. It provides basic arithmetic operations through a web interface and an API.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-calculator.git
   cd simple-calculator
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the calculator application:

```
python src/simple_calculator/app.py
```

The application will be available at `http://localhost:8000`.

## API Usage

The calculator API can be accessed via HTTP POST requests to `http://localhost:8000/calculate`.

Example request:
```
POST /calculate
Content-Type: application/x-www-form-urlencoded

num1=5&num2=3&operation=add
```

Supported operations: `add`, `subtract`, `multiply`, `divide`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

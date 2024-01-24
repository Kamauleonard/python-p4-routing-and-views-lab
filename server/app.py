#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string_param>')
def print_string(string_param):
    print(f"{string_param}")
    return f"{string_param}"

@app.route('/count/<int:int_param>')
def count(int_param):
    numbers = '\n'.join(str(num) for num in range(int_param))
    return f"{numbers}\n"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = perform_math_operation(num1, operation, num2)
    return f"{result}"

def perform_math_operation(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Cannot modulo by zero"
        return num1 % num2
    else:
        return "Invalid operation"

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
 
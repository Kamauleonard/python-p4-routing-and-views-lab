from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/hello')
def print_hello():
    text = 'hello'
    print(text)  # Print to console
    return text  # Return the plain text

@app.route('/count/<int:number>')
def count(number):
    numbers_list = '\n'.join(str(i) for i in range(number + 1))
    return numbers_list  # Return plain text

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return str(result)  # Return the result as plain text

if __name__ == '__main__':
    app.run(port=5555, debug=True)

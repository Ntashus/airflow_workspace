def calculator(num1, num2, action):

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error"
        return x / y

    actions = {"+": add, "-": subtract, "*": multiply, "/": divide}

    if action in actions:
        return actions[action](num1, num2)
    else:
        return "Error"


x = int(input("Write a first number: "))
y = int(input("Write a second number: "))
operation = input("Choose from: +, -, *, /: ")


result = calculator(x, y, operation)
print(f"My_result: {result}")

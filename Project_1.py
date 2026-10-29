def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: zero se divide nahi kar sakte."
        return num1 / num2
    else:
        return "Error: valid operation chuno (+, -, *, /)."


print("=== Calculator App ===")

try:
    number1 = float(input("Pehla number dalo: "))
    number2 = float(input("Doosra number dalo: "))

    operation = input("Operation chuno (+, -, *, /): ").strip()

    result = calculate(number1, number2, operation)
    print("Result:", result)

except ValueError:
    print("Error: please valid number dalo.")
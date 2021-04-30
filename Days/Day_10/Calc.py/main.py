from os import system
import art

# Addition
def add(n1, n2):
    """Takes to numbers as inputs and returns their sum"""
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    """Takes to numbers as inputs and returns their difference"""
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    """Takes to numbers as inputs and returns their product"""
    return n1 * n2

# Division
def divide(n1, n2):
    """Takes to numbers as inputs and returns their quotient"""
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide 
}
def calculator():
    system("clear")
    print(art.logo)
    num1 = float(input("Enter the first number: "))

    cont = True
    while cont:
        
        for symbols in operations:
            print (symbols)
        operation_symbol = input("Pick an operation from the above line: ")    
        num2 = float(input("Enter the next number: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"\n{num1} {operation_symbol} {num2} = {answer} ")

        if input(f"Press Enter/Return key to continue the calculation with {answer}\nOr any other key to start a new calculation") == "":
            num1 = answer
            system("clear")
        else:
            cont = False
            calculator()

calculator()
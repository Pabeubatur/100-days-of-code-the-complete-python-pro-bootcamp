import art

def add(n1, n2):
    """
    Adds two number and return the result
    :param n1:
    :param n2:
    :return:
    """
    #Example of docstring
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# my_favourite_calculation = add
# print(my_favourite_calculation(3,5))

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

# we can store functions as key values as long as we don't call them using parentheses()
operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

# in order to use a function inside a key, we use
# operations["+"](n1=5, n2=10)

print(art.logo)

# these variables are only used to initialize
# this variable is used to enter the loop (and in this program we never exit)
calculator_on =  True
# this variables serves as a switch to input first_number or use the previous result as the first_number
continue_operation = False
# so the IDE doesn't point that the result variable is out of reach. But It works without It anyway
result = 0

while calculator_on:
    if continue_operation:
        first_number = result
    else:
        # we clean the previours result and start a fresh one
        # this variable is repetitive in this code
        result = 0
        first_number = float(input("What is the first number?   "))

    # print operation symbols
    for operation in operations:
        print(operation)

    operation_user = input("Pick an operation:    ")

    # Both number are casted to float, because we have division operations.
    second_number = float(input("What is the next number?   "))

    # these block can be summarised with:
    # result = operations[operation_user](n1=first_number, n2=second_number)
    # but this way we have better control of every instance
    if operation_user == "+":
        result = operations["+"](first_number, second_number)
    elif operation_user == "-":
        result = operations["-"](first_number, second_number)
    elif operation_user == "*":
        result = operations["*"](first_number, second_number)
    elif operation_user == "/":
        result = operations["/"](first_number, second_number)
    else:
        print("undefined")

    print(f"{first_number} {operation_user} {second_number} = {result:.2f}")

    # Depending of this variable, we will iteratite from the first number input or we will skip it
    new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:    ").lower()

    if new_calculation == "y":
        continue_operation = True
    elif new_calculation == "n":
        continue_operation = False
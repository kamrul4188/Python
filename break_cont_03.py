terminate_program = False

while not terminate_program:
    number1 = input("Enter a number : ")
    number1 = int(number1)
    number2 = input("Enter another number: ")
    number2 = int (number2)

    while True:
        operation = input("Please add/sub or quit to exit: ")
        if operation == "quit":
            break
        if operation not in ["add", "sub"]:
            print("unknown operation")
            continue
        if operation == "add":
            print("Result is ", number1+number2)
            break
        if operation == "sub":
            print("Result is ", number1 - number2)
            break
            

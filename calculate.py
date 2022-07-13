import sys
if(len(sys.argv) != 4):
    print("input two operands and one operation")
else:
    firstOperand = sys.argv[1]
    secondOperand = sys.argv[3]
    operation = sys.argv[2]
    print(len(sys.argv))
    result = 0
    setOperations = set(['+', '-', '*', '/'])
    if((firstOperand.isdigit() != True) or (secondOperand.isdigit() != True)):
        print("The operands must be number")
    elif((operation in setOperations) != True):
        print("The operation must be: +, -, *, /")
    else:
        firstOperand = int(firstOperand)
        secondOperand = int(secondOperand)
        if(operation == "+"):
            result = firstOperand + secondOperand
        elif(operation == "-"):
            result = firstOperand - secondOperand
        elif(operation == "*"):
            result = firstOperand * secondOperand
        elif(operation == "/"):
            if(secondOperand == 0):
                result = "can't divide by zero"
            else:
                result = firstOperand / secondOperand
        print(result)
num1 = input("enter first num: ")
num2 = input("enter second num: ")
num1 = int(num1)
num2 = int(num2)
operation = input("select the operation: ")
if operation == "+":
    res = num1 + num2
    print("result: ", res)
elif operation == "-":
    res = num1 - num2
    print("result: ", res)
elif operation == "*":
    res = num1 * num2
    print("result: ", res)
elif operation == "/":
    res = num1 / num2
    print("result: ", res)
else:
    if operation == "/":
        num2 = 0
        print('error')

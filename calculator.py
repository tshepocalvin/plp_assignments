num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
opr = input("Enter one of the following(+, -, *, /): ")

if opr == "+":
    output = num1 + num2

elif opr == "-":
    output = num1 - num2

elif opr == "*":
    output = num1 * num2

elif opr == "/":
    if num2 != 0:
        output = num1 / num2

    else:
        output = "Can't divide by Zero!"

else:
    print("Invalid operation")

print("Output: ", output)
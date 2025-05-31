x = int(input("Enter value of X : "))
y = int(input("Enter value of Y : "))

op = input("Enter operator (+, -, *, /) : ") # + - / *

if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    print(x / y)
else :
    print("Invalid Operation...")

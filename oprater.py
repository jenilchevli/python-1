s = int(input("Enter value of X : "))
j = int(input("Enter value of Y : "))

op = input("Enter operator (+, -, *, /) : ")

if op == '+':
    print(s + j)
elif op == '-':
    print(s - j)
elif op == '*':
    print(s * j)
elif op == '/':
    print(s / j)
else :
    print("Invalid Operation...")

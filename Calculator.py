## Calculator
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
op=input("Enter the operator:")
if op=="+":
    print("Sum:",a+b)
elif op=="-":
    print("Subtraction:",a-b)
elif op=="*":
    print("Multiplication:",a*b)
elif op=="/":
    print("Division:",a/b)
else:
    print("Remainder:",a%b)

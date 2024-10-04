#match case is same as switch in python
#calculator
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
op=input("Enter the operator:")
match(op):
    case '+':
        print("sum:",a+b)
    case '-':
        print("Sub:",a-b)
    case '*':
        print("Mul:",a*b)
    case '/':
        print("div:",a/b)
    case '_': #means default case
        print("Remainder:",a%b)
## x+y,x-y,x*y,x/y,x%y,x**e,x**2,x**3,x**(1/2) ,x//y floor division only int part
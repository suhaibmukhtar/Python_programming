num=int(input("Enter the number::"))
if num<0:
    print("Factorial of Negative Numbers doesn't exist")
else:
    fact=1
    n=num
    while num>0:
        fact=num*fact
        num=num-1
    print(f"Factorial of a {n} is equal to::{fact}")
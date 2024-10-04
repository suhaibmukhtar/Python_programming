num=int(input("Enter the number::"))
sum=0
while num>0:
    rem=num%10
    num=int(num/10)
    sum+=rem
print(f"The Sum of Digits of Number::{sum}")
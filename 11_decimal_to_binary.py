num=int(input("Enter the decimal number::"))
binary,p=0,1
while num>0:
    rem=num%2
    binary=binary+rem*p
    num=int(num/2)
    p*=10
print(f"Binary Equivalent of a Decimal is:{binary}")

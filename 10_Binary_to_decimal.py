num=int(input("Enter the Binary number::"))
dec,mul=0,1
while num>0:
    rem=num%10
    dec=dec+mul*rem
    num=int(num/10)
    mul*=2
print(f"The Decimal Equivalent of Binary is::{dec}")
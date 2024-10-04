#A loop is required when we want to execute a statement or set of statement several times
# examples are while,do-while,for-loop
## Every loop requires initialization,condition and flow
## While-loop is an entry control loop:

##q1 write numbers from 1 to 10
i=0
while(i<=10):
    print(i,end=" ")
    i+=1
print("\n")

##q2 print numbers in reverse order with a difference of 2
k=10
while(k>=0):
    print(k,end=" ")
    k-=2
## wap to print sum of digits of a number
num=int(input('Enter the number:'))
sum=0
while(num>0):
    rem=num%10
    num=int(num/10)
    sum+=rem
print("sum of digits:",sum)
## to find factorial of a number
num=int(input("Enter the number:"))
fact=1
while(num>0):
    fact*=num
    num=num-1
print("Factorial of number:",fact)
#binary to decimal conversion
num=int(input('enter the binary_number:'))
decimal=0
p=1
while(num>0):
    rem=num%10
    decimal+=rem*p
    p*=2
    num=int(num/10)
print(decimal)






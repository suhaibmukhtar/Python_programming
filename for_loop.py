# # #to print numbers from 1 to 10
# # for i in range(1,11):
# #     print(i,end=" ")
# # print("\n")
# #
# # ## program to print numbers in reverse order
# # for i in range(10,0,-1):#start,end,step_size
# #     print(i,end=" ")
# # print("\n")
# # ## to print numbers in reverse order with a difference of 2
# # for i in range(10,0,-2):
# #     print(i,end=" ")
# # ## Multiply two positive operators without using * operator
# a=int(input("Enter the number:"))
# b=int(input("Enter the number2:"))
# mul=0
# for i in range(b):
#     mul+=a
# print("Multiplication of ",a,"and",b,"is:",a*b)
#Find the sum of series 1+2+4+7+11+16+...
j=0
n=int(input("Enter the number of terms:"))
sum=0
term=1
for i in range(1,n+1):
    sum+=sum+term
    term+=i
print("sum:",sum)
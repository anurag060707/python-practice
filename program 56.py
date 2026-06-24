# a Python program to find the factorial of a given number. 
num=int(input("enter number to find factorial:"))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(fac)    
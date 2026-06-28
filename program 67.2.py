#a Python program to find the LCM (Least Common Multiple) of two numbers.
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
a=num1
b=num2
if(a<b):
    smaller=a
else:
    smaller=b
for i in range(1,smaller+1):
    if(a%i==0 and b%i==0):
        HCF=i
LCM=num1*num2//HCF
print("hcf of two number:",HCF)
print("lcm of two number=",LCM)
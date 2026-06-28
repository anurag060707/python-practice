# a Python program to find the GCD (Greatest Common Divisor) of two numbers.
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if(num1<num2):
    smaller=num1
else:
    smaller=num2
for i in range(1,smaller+1):
    if(num1%i==0 and num2%i==0):
        hcf=i
print("hcf of two number=",hcf)
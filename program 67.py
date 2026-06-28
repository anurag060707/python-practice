#a Python program to find the LCM (Least Common Multiple) of two numbers.
num1=int(input("enter number:"))
num2=int(input("enter number:"))
a=num1
b=num2
while b !=0:
    a,b=b,a%b
hcf=a
lcm=num1*num2//a
print("hcf of two number=",hcf)
print("gcd of two number=",lcm)
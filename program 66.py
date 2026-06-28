# a Python program to find the GCD (Greatest Common Divisor) of two numbers.
num1=int(input("enter number:"))
num2=int(input("enter number:"))
while num2!=0:
    num1,num2=num2,num1%num2
print(num1)

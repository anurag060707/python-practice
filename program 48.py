# a Python program to find the largest among four numbers.
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
num4=int(input("enter fourth number:"))
if(num1>num2 and num1>num3 and num1>num4):
    print("num1 is largest")
elif(num2>num1 and num2>num3 and num2>num4):
    print("num2 is largest")
elif(num3>num1 and num3>num2 and num3>num4):
    print("num3 is largest")
else:
    print("num4 is largest")            
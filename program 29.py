#program to find the largest among three numbers entered by the user. 
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
num3=float(input("enter third number:"))
if(num1<=num2 and num1>=num3):
    print("num1 is greater")
elif(num2>=num1 and num2>=num3):
    print("num2 is greater")
else:
    print("num3 is greater")

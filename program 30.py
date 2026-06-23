#program to find the smallest among three numbers entered by the user.
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
num3=float(input("enter third number:"))
if(num1<num2 and num1<num3):
    print("num1 is smallest")
elif(num2<num1 and num2<num3):
    print("num2 is smallest")
else:
    print("num3 is smallest")        
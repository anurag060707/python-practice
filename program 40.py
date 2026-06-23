#Python program to create a simple calculator using if-elif-else for addition,subtraction, multiplication, and division
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
print("choose for calculating:")
print("1 for addition:")
print("2 for subtract:")
print("3 for multiply:")
print("4 for division:")
choice=int(input("enter your choice:"))
if(choice==1):
    print("addition=",num1+num2)
elif(choice==2):
    print("subtract=",num1-num2)
elif(choice==3):
    print("multiply=",num1*num2)
elif(choice==4):
    print("division=",num1/num2)
else:
    print("wrong choice:")
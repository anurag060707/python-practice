# Python program to check whether a number is divisible by both 5 and 11. 
num=int(input("enter number:"))
if(num%5==0) and (num%11==0):
    print("both are divisible by 5 and 11")
else:
    print("any one is not divisible by 5 and 11")    
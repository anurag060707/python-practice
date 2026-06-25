# a Python program to find the product of digits of a number. 
num=int(input("enter number:"))
pro=1
while(num>0):
    digit=num%10
    pro=pro*digit
    num//=10
print(pro)
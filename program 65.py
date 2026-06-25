# a Python program to check whether a number is a palindrome number.
num=int(input("enter number:"))
t=num
rev=0
while(num>0):
    rev=rev*10+num%10
    num=num//10
if(rev==t):
    print("palindrome")
else:
    print("not palindrome")
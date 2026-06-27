#a Python program to check whether a string is a palindrome. 
char=input("enter string:")
temp=char
x=char[-1::-1]
if(temp==x):
    print("palindrome")
else:
    print("not palindrome")

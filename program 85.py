#a Python program to remove all spaces from a string.
char=input("enter string:")
new=""
for i in range(len(char)):
    if(char[i] !=" "):
        new=new+char[i]
print("after removing spaces=",new)        
        

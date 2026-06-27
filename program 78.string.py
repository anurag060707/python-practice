# a Python program to convert a string to lowercase. 
char=input("enter string in uppercase:")
if(char.isupper()):
    result=""
    for i in char:
        result+=chr(ord(i)+32)
    print("string in lowercase=",result)
else:
    print("input is not fully in uppercase:")

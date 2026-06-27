# a Python program to convert a string to uppercase. 
char=input("enter string in lowercase:")
result=""
for ch in char:
    result+=chr(ord(ch)-32)
print("string in uppercase=",result)

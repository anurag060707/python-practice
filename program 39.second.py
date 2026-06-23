# Python program to check whether a character is uppercase or lowercase
ch=input("enter character:")
ascii_value=ord(ch)
if(ascii_value>=97 and ascii_value<=122):
    print("lowercase")
elif(ascii_value>=65 and ascii_value<=90):
    print("uppercase")
else:
    print("given input is not character")
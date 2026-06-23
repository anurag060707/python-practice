#Python program to check whether a character entered by the user is a vowel or a consonant
ch=input("enter character:")
ascii_value=ord(ch)
if(ascii_value>=65 and ascii_value<=90) or (ascii_value>=97 and ascii_value<=122):
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
        print("given character is vowel")
    else:
        print("given input is not vowel")    
else:
    print("given input is not character")        
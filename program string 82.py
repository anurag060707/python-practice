# a Python program to count the number of consonants in a string. 
char=input("enter string:")
con=0
for ch in char:
    if(ch>="a" and ch<="z" or ch>="A" and ch<="Z"):
        if(ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u" and ch!="A" and ch!="E" and ch!="I" and ch!="O" and ch!="U"):
            con=con+1
print("number of consonants=",con)
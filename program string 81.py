#a Python program to count the number of vowels in a string.
char=input("enter string:")
count=0
for ch in char:
     if(ch=="a" or ch=="e" or ch=="i" or char=="0" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
        count+=1
print("number of vowel=",count)


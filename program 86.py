# a Python program to count the frequency of each character in a string. 
string=input("enter string:")
for ch in string:
    count=0
    for x in string:
        if ch==x:
            count+=1
    print("frequency of character",ch,"=",count)    


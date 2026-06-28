#a Python program to count the occurrences of a specific character in a string.
string=input("enter string:")
char=input("enter character:")
count=0
for i in range(len(string)):
    if string[i]==char:
        count+=1
print("frequency of char=",count)        
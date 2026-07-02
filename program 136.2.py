#a Python function to reverse a string.
#method 2
def rev(string):
    for i in range(len(string)-1,-1,-1):
        print(string[i],end="")
string=input("enter string:")
rev(string)


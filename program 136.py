#a Python function to reverse a string.
def rev(string):
    x=string[-1::-1]
    print("reverse of string=",x)
string=input("enter string:")
rev(string)    
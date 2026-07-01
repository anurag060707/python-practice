# a Python program to remove duplicates from a list using a set.
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
print("the original list:") 
y=list(set(a))
print(y)   
#a Python program to create a list and display all its elements.
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements:"))
    a.append(x)
for i in range(n):
    print(a[i],end=" ")    
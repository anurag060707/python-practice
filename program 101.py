#a Python program to create a tuple containing five elements and display it. 
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of elements:"))
    a.append(x)
x=tuple(a) 
print(x)  
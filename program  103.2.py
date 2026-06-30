# a Python program to find the length of a tuple. 
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
y=tuple(a)
count=0
for i in range(len(y)):
    count+=1
print("length of tuple=",count)        
# a Python program to count unique elements in a list using a set.
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
y=list(set(a))
count=0   # or count=len(y)
for i in range(len(y)):
    count+=1
print("number of elements in list=",count)        
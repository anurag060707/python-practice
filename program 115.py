# a Python program to find the intersection of two sets. 
a=set()
b=set()
n1=int(input("enter length of set1:"))
n2=int(input("enter length of set2:"))
for i in range(n1):
    x1=int(input("enter elements of set1:"))
    a.add(x1)
for i in range(n2):
    x2=int(input("enter elements of set2:"))
    b.add(x2) 
d=a&b #or d=a.intersection(b)
print("intersection of two set=",d)       
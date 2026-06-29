# a Python program to sort a list in ascending order. 
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
a.sort()
print("after sorting in ascending order=",a)
  
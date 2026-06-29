#a Python program to calculate the sum of all elements in a list. 
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
total=0
for i in range(n):
    total+=a[i]
print("sum of elements=",total)        
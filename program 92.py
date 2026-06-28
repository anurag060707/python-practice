# a Python program to find the largest element in a list. 
a=[]
n=10
for i in range(n):
    x=int(input("enter number:"))
    a.append(x)
print("elements of list:")
for i in range(n):
    print(a[i])
max=a[0]
for i in range(n):
    if(a[i]>=max):
        max=a[i]
print("largest number in list=",max)        

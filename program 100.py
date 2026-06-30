#a Python program to find the second largest element in a list.
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
max=a[0]
for i in range(n):
    if(a[i]>max):
        max=a[i]
a.remove(max)
max2=a[0]
for i in range(n-1):
    if(a[i]>max2):
        max2=a[i]
print("second largest number in list=",max2)                    
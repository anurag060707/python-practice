#a Python program to sort a list in descending order. 
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
for i in range(n):
    for j in range(i+1,n):
        if(a[i]<a[j]):
            temp=a[j]
            a[j]=a[i]
            a[i]=temp 
print("after descending order=",a)               
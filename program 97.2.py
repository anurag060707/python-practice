# a Python program to sort a list in ascending order. 
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements fo list:"))
    a.append(x)
for i in range(n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("after ascending=",a)               
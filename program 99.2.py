#a Python program to reverse a list.
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
b=[]    
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print("after reverse elements of list=",b)         

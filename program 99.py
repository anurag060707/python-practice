# a Python program to reverse a list. 
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list:"))
    a.append(x)
y=a[-1::-1]
print("reverse of list elements=",y)    
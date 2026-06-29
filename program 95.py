#a Python program to calculate the average of all elements in a list. 
list=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements:"))
    list.append(x)
sum=0
for i in range(n):
    sum+=list[i]
average=sum/n
print("average of elements=",average)            
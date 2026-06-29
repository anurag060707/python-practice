#a Python program to find the smallest element in a list. 
list=[]
n=10
for i in range(n):
    x=int(input("enter elements:"))
    list.append(x)
print("elements of list:")
for i in range(n):
    print(list[i])
min=list[0]
for i in range(n):
    if(list[i]<=min):
        min=list[i] 
print("the smallest number of list=",min)               
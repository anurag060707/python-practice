# a Python program to find the index of a specified element in a tuple.
tuple=(1,5,4,6,77,3,2)
elements=int(input("enter elements to find index:"))
flag=1
for i in range(len(tuple)):
    if(tuple[i]==elements):
       print("index of elements=",i)
       flag=0
       break
if(flag==1):
    print("elements not found:")       


    
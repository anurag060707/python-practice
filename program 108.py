#a Python program to check whether an element exists in a tuple.
tuple=(1,2,3,4,5,3)
element=int(input("enter elements:"))
flag=0
for i in range(len(tuple)):
    if tuple[i]==element:
        print("exists")   
        flag=1
        break
if(flag==0):
    print("does not exists")        

      
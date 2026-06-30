# a Python program to count the occurrences of an element in a tuple. 
tuple=(1,2,5,4,1,6,7,1)
elements=int(input("enter elements:"))
count=0
for i in range(len(tuple)):
    if tuple[i]==elements:
        count+=1
print("occurrences of an elements=",count)        

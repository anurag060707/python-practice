#a Python program to remove duplicate elements from a list
list=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements:"))
    list.append(x)
result=[]    
for i in list:
    if i not in result:
        result.append(i)
print("after removing duplicate elements=",result)        

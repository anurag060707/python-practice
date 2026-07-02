# a Python function that accepts a list and returns the maximum element.
def maximum(a,n):
    max=a[0]
    for i in range(n):
        if(a[i]>max):
            max=a[i]
    return max
a=[]
n=int(input("enter length of list:"))
for i in range(n):
    x=int(input("enter elements of list"))
    a.append(x)    
result=maximum(a,n)
print(result)


        
    
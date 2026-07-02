#a Python function to calculate the sum of all elements in a list. 
def add(a):
    sum=0
    for i in range(n):
        sum+=a[i]
    print("after calculating tha sum of all elements=",sum)
a=[]
n=int(input("enter length of list"))
for i in range(n):
    x=int(input("enter elements of list"))
    a.append(x)
add(a)            
        
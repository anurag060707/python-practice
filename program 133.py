#a Python function to check whether a number is prime.
def prim(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        print("prime")
    else:
        print("not prime")    
n=int(input("enter number to find"))
prim(n)               
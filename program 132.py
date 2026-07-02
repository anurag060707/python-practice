#a Python function to find the factorial of a number.
def fact(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    print("factorial of a number=",fac)
n=int(input("enter number"))    
fact(n)

        
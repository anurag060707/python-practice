# a Python program to print all palindrome numbers between 1 and 1000. 
for i in range(1,1001):
    t=i
    rev=0
    while(t>0):
        rev=rev*10+t%10
        t=t//10
    if(i==rev):
        print(i)    

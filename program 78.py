#a Python program to print all Armstrong numbers between 1 and 1000.
for num in range(1,1001):
    sum=0
    temp=num
    while(temp>0): 
        digit=temp%10
        sum=sum+digit*digit*digit
        temp=temp//10
    if(num==sum):
         print(num)        
    
        

    
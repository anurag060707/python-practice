# a Python program to check whether a number is an Armstrong number. 
num=int(input("enter number:"))
t=num
sum=0
while(num>0):
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if(sum==t):
    print("armstrong")
else:
    print("not armstrong")
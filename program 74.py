#a Python program to count even and odd digits in a number. 
num=int(input("enter number:"))
even=0
odd=0
while(num>0):
    digit=num%10
    if(digit%2==0):
        even+=1
    else:
        odd+=1
    num=num//10    
print("even=",even, "and","odd",odd)            
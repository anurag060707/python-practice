#a Python program to count the frequency of a digit in a number.
num=int(input("enter number:"))
fre=int(input("enter a digit"))
count=0
while(num>0):
    digit=num%10
    if(digit==fre):
        count+=1
    num//=10
print("frequency of number=",count)    
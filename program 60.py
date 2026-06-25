#a Python program to count the number of digits in a given number. 
num=int(input("enter number:"))
count=0
while(num>0):
    num=num//10
    count+=1
print(count)

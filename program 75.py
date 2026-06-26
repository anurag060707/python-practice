# a Python program to find the largest digit in a number.
num=int(input("enter number:"))
largest=0
while(num>0):
    digit=num%10
    if(digit>largest):
        largest=digit
    num=num//10
print(largest)        
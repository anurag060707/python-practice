# a Python program to find the smallest digit in a number. 
num=int(input("enter number:"))
smallest=9
while(num>0):
    digit=num%10
    if(digit<smallest):
        smallest=digit
    num=num//10
print(smallest)        
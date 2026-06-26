#a Python program to find all factors of a given number.
num=int(input("enter number:"))
print("factor")
for i in range(1,num+1):
    if(num%i==0):
        print(i) 
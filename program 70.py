#Write a Python program to print the following pattern:
num=int(input("enter number:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if(j<=num-i):
            print("*",end="")
    print()        
#Write a Python program to print the following pattern: 
for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print("*",end="")
    print()        
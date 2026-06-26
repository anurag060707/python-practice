# a Python program to calculate the power of a number using loops. 
base=int(input("enter base:"))
power=int(input("enter power:"))
result=1
for i in range(power):
    result=result*base
print(result)    
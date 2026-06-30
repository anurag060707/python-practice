#a Python program to find the maximum and minimum value in a tuple.
tuple=(1,3,0,5,4,2,8,7,9)
max=tuple[0]
for i in range(len(tuple)):
    if(tuple[i]>max):
        max=tuple[i]
min=tuple[0]
for i in range(len(tuple)):
    if(tuple[i]<min):
        min=tuple[i]
print("the maximum value=",max,"and","the minimum value=",min)                
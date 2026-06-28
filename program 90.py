#a Python program to find the longest word in a sentence.
sentence=input("enter sentence:")
x=sentence.split()
max=x[0]
for i in range(len(x)):
    if(len(x[i])>len(max)):
        max=x[i]
print("largest word in sentence=",max)        
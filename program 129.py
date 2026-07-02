# a Python program to count the frequency of each character in a string using a dictionary. 
string=input("enter string:")
frequency={}
for ch in string:
    if ch in frequency:
        frequency[ch] +=1
    else:
        frequency[ch]=1
print("character frequency")        
for key,value in frequency.items():
    print(key,value)            
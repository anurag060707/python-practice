# a Python function to count vowels in a string.
def string(a):
    count=0
    for i in range(len(a)):
        if (a[i]>="a" and a[i]<="z") or (a[i]>="A" and a[i]<="Z"):
            if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
                count+=1
    print("number of vowel in string=",count)
a=input("enter string:")         
string(a)           
                 

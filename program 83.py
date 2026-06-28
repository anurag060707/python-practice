#a Python program to count the number of words in a sentence.
sentence=input("enter sentence:")
count=1
for word in sentence:
    if(word==" "):
        count+=1
print("number of words=",count)   

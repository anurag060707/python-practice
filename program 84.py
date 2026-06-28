# a Python program to replace a word in a string with another word.
sentence=input("enter sentence:")
old_word=input("enter old word:")
new_word=input("enter new_word:")
words=sentence.split()
for i in range(len(words)):
    if(words[i]==old_word):
        words[i]=new_word
result=""
for word in words:
    result+=word+" "
print("updated sentence=",result)    
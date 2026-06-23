# a Python program to determine the day of the week based on a number entered by the ser (1–7). 
print("choose 1-7 to print day name:")
print("1 for sunday:")
print("2 for monday:")
print("3 for tuesday:")
print("4 for wednesday:")
print("5 for thursday:")
print("6 for friday:")
print("7 for saturday:")
choice=int(input("enter your choice 1-7:"))
if(choice==1):
    print("sunday")
elif(choice==2):
    print("monday")
elif(choice==3):
    print("tuesday")
elif(choice==4):
    print("wednesday")
elif(choice==5):
    print("thursday")
elif(choice==6):
    print("friday")
elif(choice==7):
    print("saturday")
else:
    print("wrong choice")

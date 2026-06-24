# a Python program to check whether a triangle is valid based on the lengths of its three sides.
side1=float(input("enter first side:"))
side2=float(input("enter second side:"))
side3=float(input("enter third side:"))
if(side1+side2>side3 and side1+side3>side2 and side2+side3>side1):
    print("triangle is valid")
else:
    print("triangle is not valid")    

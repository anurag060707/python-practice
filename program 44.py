# a Python program to classify a triangle as: 1. Equilateral 2. Isosceles 3. Scalene 
side1=float(input("enter first side:"))
side2=float(input("enter second side:"))
side3=float(input("enter third side:"))
if(side1==side2==side3):
    print("Equilateral")
elif(side1==side3 or side2==side3 or side1==side2):
    print("isosceles")        
else:
    print("scalene")

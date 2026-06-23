#Python program to calculate the total, percentage, and average marks of five subjects
hindi=float(input("enter marks of hindi:"))
english=float(input("enter marks of english:"))
math=float(input("enter marks of math:"))
physics=float(input("enter marlks of physics:"))
chemistry=float(input("enter marks of chemistry:"))
#average of five subjects
average=(hindi+english+math+physics+chemistry)/5
total_marks=hindi+english+math+physics+chemistry
percentage=total_marks/500*100
print("average of five subjects=",average,"\npercentage of five subjects=",percentage)
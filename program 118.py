#a Python program to check whether one set is a subset of another.
set1={1,2,3,4,5}
set2={1,2,3,4,5,6,7,8,9}
if(set1<=set2):  #or set1.issubset(set2):
    print("set1 is a subset of set2:")
else:
    print("set1 is nota subset of set2:")

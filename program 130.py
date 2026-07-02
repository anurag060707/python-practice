#a Python program to merge two dictionaries into a single dictionary. 
dict1={"name":"anurag sharma","age":19}
dict2={"city":"hardoi","college":"ignou"}
dict1.update(dict2) # or dict1|dict2 or dict1.union.dict2
print("after merging into a single dictionary=",dict1)
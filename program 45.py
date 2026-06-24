# a Python program to calculate discount according to the following rules: ● Purchase above ₹5000 → 20% discount ● Purchase above ₹3000 → 10% discount ● Otherwise → No discount 
purchase=int(input("enter amount to calculate discount:"))
if(purchase>5000):
    discount=purchase*20/100
    print("20 percentage discount=",discount)
elif(purchase>3000):
    print("10 percentage discount=",purchase*10/100)
else:
    print("no discount")        
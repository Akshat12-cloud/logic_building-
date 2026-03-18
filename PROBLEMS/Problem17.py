# Take electricity units consumed and calculate the bill as per slabs (using if-else). 
'''First 100 units → ₹5 per unit

Next 100 units (101–200) → ₹7 per unit

Above 200 units → ₹10 per unit '''

units=int(input("enter the unit of electricity bill:"))
if(units<=100):
    bill=units*5
    print(f"the bill of {units} units is {bill}")
elif(units<+200):
    bill=(units*5)+(units-100)*7
    print(f"the bill of {units} unit is {bill}")
else:
    bill=(units*5)+(units-100)*7 +(units-200)*10   
    print(f"the bill of {units } unit is {bill}") 
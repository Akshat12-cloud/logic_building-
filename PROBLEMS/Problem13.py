# Take income and age, and check if eligible for tax (age > 18 and income > 5 L). 
income=int(input("enter your income in lakhs:"))
age=int(input("enter your age:"))
if (age>18 and income>500000):
    print("you are eligible for tax")
else:
    print("you are not eligible for tax")
    
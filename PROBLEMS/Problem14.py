#Take two numbers and check if both are positive and their sum is less than 100.
num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
if (num1>0 and num2>0) and ((num1 +num2) <100):
    print("both numbers are positive and their sum is less than 100")
elif (num1>0 and num2>0) and ((num1 +num2) >100):
    print("both number are positive but there sum is more than 100")
elif(num1>0 and num2<0) or (num1<0 and num2>0):
    print("one of the number is negative")
else :
    print("both are negative")



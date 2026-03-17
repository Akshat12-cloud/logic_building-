#Take five numbers and print the median value (neither maximum nor minimum).
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
num4=int(input("enter the fourth number:"))
num5=int(input("enter the fifth number:"))
num=[num1,num2,num3,num4,num5]
num.sort()
print(num)
median=num[(len(num))//2]
print("the median value is",median)
print("the length of the list is",len(num))





#Print all numbers between a and b divisible by 7
a=int(input("enter the the number a:"))
b=int(input("enter the number b:"))
for i in range(a,b+1):
    if (i%7==0):
        print(i)
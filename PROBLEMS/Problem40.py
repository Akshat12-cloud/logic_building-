#Check if a number is a perfect number.
n=int(input("enter the number :"))
sum=0
temp=n
for i in range(1,n):
    if (n%i==0):
        sum+=i
if (temp==sum):
    print("the number is a perfect number")
else:
    print("the number is not a perfect number")
            

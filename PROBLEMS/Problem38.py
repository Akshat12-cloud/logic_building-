#Find the sum of digits of a number
n=int(input("enter the number"))
sum=0
temp=n
while n>0:
    digit=n%10
    sum+=digit
    n//=10
print(f"the sum of the number {temp} is {sum}")
    
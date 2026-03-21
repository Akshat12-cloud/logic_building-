#Count the number of digits in a given number
n=int(input("Enter the number :"))
temp=n
count=0
while n!=0: 
    n//=10 
    count+=1
print(f'the number of digits in the {temp} is {count}')         
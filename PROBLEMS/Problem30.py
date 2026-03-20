#Print the sum of first n natural numbers. 
n=int(input("enter the natural number"))
sum=0
for i in range(1,n+1):
    sum+=i
    i+=i
print(f"the sum of first {n} natural numaber is {sum}  ")

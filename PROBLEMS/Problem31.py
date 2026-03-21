#Print the sum of all even numbers up to n
n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    if (i%2==0):
        sum+=i
    
print(f"the sum of the even number upto {n} terms is {sum}  ")


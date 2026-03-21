# Print the factorial of a given number.
n=int(input("enter thr number for its factorial:"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(f"the factorial of {n} is {factorial}")    
     
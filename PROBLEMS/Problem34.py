# Print the product of digits of a given number.  
n=int(input("Enter the number :"))
product=1
for i in range(1,n+1):
    if n>0:
        digit=n%10
        product*=digit
        n//=10
print(f"the product of the digits is {product}")        

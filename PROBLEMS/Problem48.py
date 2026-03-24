# Find HCF (GCD) of two numbers using loops.
a=int(input("enter trhe number a:"))
b=int(input("enter the number b:")) 
hcf=1
for i in range(1,min(a,b)+1):       
    if (a%i==0 and b%i==0):
        hcf=i
print("HCF of", a, "and", b, "is:", hcf)
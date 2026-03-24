#Find LCM of two numbers using loops.
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
lcm=1
for i in range(max(a,b),a*b+1):
    if (i%a==0 and i%b==0):
        lcm=i
        break
print("LCM of", a, "and", b, "is:", lcm)
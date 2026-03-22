#Print the reverse of a given number.
n=int(input("enter the number : "))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(f"the reverse of the number is {rev}")


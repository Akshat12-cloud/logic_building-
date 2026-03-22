#Check if a number is a palindrome.
n=int(input("enter the number : "))
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
if original==rev:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")

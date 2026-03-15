#Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.

num = int(input("Enter a 3-digit number: "))

first = num // 100
middle = (num // 10) % 10
last = num % 10

if middle > first and middle > last:
    print("The middle digit is the largest.")
elif middle < first and middle < last:
    print("The middle digit is the smallest.")
else:
    print("The middle digit is neither the largest nor the smallest.")

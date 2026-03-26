#Find the smallest and largest digit in a given number.
num = int(input("Enter a number: "))
smallest_digit = 9
largest_digit = 0

while num > 0:
    digit = num % 10
    if digit < smallest_digit:
        smallest_digit = digit
    if digit > largest_digit:
        largest_digit = digit
    num //= 10

print("Smallest digit:", smallest_digit)
print("Largest digit:", largest_digit)
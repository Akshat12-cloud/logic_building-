''' Take an integer (1-9999) and check if the sum of its digits is greater than the product 
of its digits. '''
num = int(input("Enter a number (1-9999): "))

temp = num
sum_digits = 0
product_digits = 1

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    product_digits *= digit
    temp //= 10

if sum_digits > product_digits:
    print("Sum of digits is greater than product of digits")
else:
    print("Sum of digits is NOT greater than product of digits")
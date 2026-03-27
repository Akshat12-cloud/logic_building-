#Print the sum of all odd digits and even digits separately in a number. 
n = int(input("Enter a number: "))

sum_odd = 0
sum_even = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit
    n //= 10

print(f"Sum of odd digits: {sum_odd}")
print(f"Sum of even digits: {sum_even}")
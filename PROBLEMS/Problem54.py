# Print all numbers whose sum of digits is even (1–100)

for i in range(1, 101):
    n = i
    sum_of_digit = 0
    
    while n > 0:
        digit = n % 10
        sum_of_digit += digit
        n //= 10
    
    if sum_of_digit % 2 == 0:
        print(i, end=" ")
#Print numbers between 1–100 whose digits add up to a multiple of 3.
for i in range(1, 101):
    n = i
    sum_of_digits = 0

    while n > 0:
        digit = n % 10
        sum_of_digits += digit
        n //= 10

    if sum_of_digits % 3 == 0:
        print(i, end=" ")
#Print all numbers from 1–n whose binary representation has an even number of 1s. 

n = int(input("Enter value of n: "))

for num in range(1, n + 1):
    temp = num
    count_ones = 0

    # Convert to binary manually
    while temp > 0:
        remainder = temp % 2
        if remainder == 1:
            count_ones += 1
        temp = temp // 2

    # Check if number of 1s is even
    if count_ones % 2 == 0:
        print(num, end=" ")
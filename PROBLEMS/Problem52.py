#Check if a number is a strong number (sum of factorials of digits = number). 
# Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Check Strong Number
num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += factorial(digit)
    temp //= 10

if sum_fact == num:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is NOT a Strong Number")
# Print sum of series 1 + 2 + 3 + ... + n recursively and display each step.
def sum_series(n):
    if n == 1:
        print("1 = 1")
        return 1
    
    result = n + sum_series(n - 1)
    print(f"{n} + sum({n-1}) = {result}")
    return result

n = int(input("Enter a number: "))
total = sum_series(n)
print("Final Sum =", total)
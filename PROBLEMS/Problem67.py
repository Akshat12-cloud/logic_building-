#Print pattern of numbers recursively (1 to n each row).
def print_numbers(num):
    if num == 0:
        return
    print_numbers(num - 1)
    print(num, end=" ")

def pattern(n):
    if n == 0:
        return
    pattern(n - 1)
    print_numbers(n)
    print()

n = int(input("Enter value of n: "))
pattern(n)


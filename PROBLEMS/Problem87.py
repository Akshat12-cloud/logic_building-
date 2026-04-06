#Count how many elements are even and odd. 
def count_even_odd(nums):
    even = 0
    odd = 0

    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


# Example usage
numbers = [2, 5, 0, 7, 8, 3, 4]
e, o = count_even_odd(numbers)

print("Even numbers:", e)
print("Odd numbers:", o)
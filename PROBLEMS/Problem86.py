#Count how many elements are positive, negative, or zero.
def count_numbers(nums):
    positive = 0
    negative = 0
    zero = 0

    for num in nums:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1

    return positive, negative, zero


# Example usage
numbers = [2, -5, 0, 7, -1, 0, 4]
p, n, z = count_numbers(numbers)

print("Positive numbers:", p)
print("Negative numbers:", n)
print("Zero numbers:", z)
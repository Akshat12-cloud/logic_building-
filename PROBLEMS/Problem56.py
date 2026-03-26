#Print all numbers that are palindromes between 1–500.
def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

for i in range(1, 501):
    if is_palindrome(i):
        print(i, end=" ")
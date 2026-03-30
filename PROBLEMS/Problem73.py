#Count vowels in a string recursively.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    if len(s) == 0:
        return 0
    else:
        if s[0] in vowels:
            return 1 + count_vowels(s[1:])
        else:
            return count_vowels(s[1:])

text = input("Enter a string: ")
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)
# Count consonants and vowels separately using recursion. 

def count_vowels_consonants(s, vowels=0, consonants=0):
    # Base case
    if len(s) == 0:
        return vowels, consonants

    # Check first character
    first_char = s[0]
    if first_char.lower() in "aeiou":
        vowels += 1
    elif first_char.isalpha():
        consonants += 1

    # Recursive call for rest of string
    return count_vowels_consonants(s[1:], vowels, consonants)

# Input
text = input("Enter a string: ")
vowel_count, consonant_count = count_vowels_consonants(text)

print("Vowel count:", vowel_count)
print("Consonant count:", consonant_count)

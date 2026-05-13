#Count how many vowels and consonants are in a string. 
s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s:
    # Convert uppercase to lowercase manually
    if ch >= 'A' and ch <= 'Z':
        ch = chr(ord(ch) + 32)

    # Check if alphabet
    if ch >= 'a' and ch <= 'z':
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
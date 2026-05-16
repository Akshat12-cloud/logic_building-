#Count how many substrings start and end with the same character (simple logic).
s = input("Enter a string: ")

freq = {}

# Count frequency of each character
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

total = 0

# Apply formula n(n+1)/2
for ch in freq:
    n = freq[ch]
    total += n * (n + 1) // 2

print("Total substrings starting and ending with same character:", total)
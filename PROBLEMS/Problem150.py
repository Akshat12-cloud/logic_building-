# Print how many words start with a vowel in a sentence. 
sentence = input("Enter a sentence: ")

words = sentence.split()
count = 0

for word in words:
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Number of words starting with a vowel:", count)
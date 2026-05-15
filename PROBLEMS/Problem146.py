#Count how many spaces are there in a sentence.
sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:
    if ch == ' ':
        count += 1

print("Number of spaces:", count)
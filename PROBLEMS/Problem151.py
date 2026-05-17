#Count how many words end with ‘s’.
sentence = input("Enter a sentence: ")

words = sentence.split()
count = 0

for word in words:
    if word[-1].lower() == 's':
        count += 1

print("Number of words ending with 's':", count)
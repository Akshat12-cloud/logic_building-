#Count how many words are in a sentence.
sentence = input("Enter a sentence: ")

count = 0

for i in range(len(sentence)):
    if sentence[i] != " " and (i == 0 or sentence[i-1] == " "):
        count = count + 1

print("Number of words:", count)
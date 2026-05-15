#Count how many times a given character appears in a string. 
string = input("Enter a string: ")
ch = input("Enter a character to count: ")

count = 0

for i in range(len(string)):
    if string[i] == ch:
        count += 1

print("Frequency of", ch, "is:", count)
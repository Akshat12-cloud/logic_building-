#Create a Python program to manage a student’s name using string operations.
#The program should:
#Take a student name as input
#Count vowels and consonants
#Reverse the name
#Check whether the name is palindrome
#Display frequency of each character
# Student Name String Analyzer

name = input("Enter student name: ")

vowels = 0
consonants = 0

# Count vowels and consonants
for ch in name.lower():

    if ch >= 'a' and ch <= 'z':

        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels += 1
        else:
            consonants += 1

print("\nTotal Vowels:", vowels)
print("Total Consonants:", consonants)

# Reverse the string
reverse = ""

for ch in name:
    reverse = ch + reverse

print("Reversed Name:", reverse)

# Palindrome check
if name.lower() == reverse.lower():
    print("Palindrome Name")
else:
    print("Not a Palindrome Name")

# Frequency of characters
print("\nCharacter Frequency:")

checked = ""

for ch in name.lower():

    if ch != " " and ch not in checked:

        count = 0

        for x in name.lower():

            if ch == x:
                count += 1

        print(ch, "=", count)

        checked += ch

print("\nProgram Finished")

#Count how many alphabets are before ‘m’ and after ‘m’ in a given string. 
s = input("Enter a string: ")

before_m = 0
after_m = 0

for ch in s:
    if ch.isalpha():          # check if character is alphabet
        ch = ch.lower()       # convert to lowercase
        
        if ch < 'm':
            before_m += 1
        elif ch > 'm':
            after_m += 1

print("Alphabets before 'm':", before_m)
print("Alphabets after 'm':", after_m)
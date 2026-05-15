#Find the frequency of each character in a string (without using a map).
string = input("Enter a string: ")

checked = []   # List to store already counted characters

for i in range(len(string)):
    count = 0
    
    # Skip if character already counted
    if string[i] in checked:
        continue
    
    for j in range(len(string)):
        if string[i] == string[j]:
            count += 1
    
    print(string[i], ":", count)
    checked.append(string[i])
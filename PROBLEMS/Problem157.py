#Print the middle character(s) of a string. 

string = input("Enter a string: ")

length = 0

# Find length without using len()
for ch in string:
    length += 1

# Check even or odd length
if length % 2 == 0:
    mid1 = (length // 2) - 1
    mid2 = length // 2

    index = 0
    for ch in string:
        if index == mid1 or index == mid2:
            print(ch, end="")
        index += 1
else:
    mid = length // 2

    index = 0
    for ch in string:
        if index == mid:
            print(ch)
        index += 1
#Print the second half of the string in reverse.
string = input("Enter a string: ")

length = len(string)

# Starting index of second half
start = length // 2

print("Second half in reverse: ", end="")

# Print second half in reverse
for i in range(length - 1, start - 1, -1):
    print(string[i], end="")

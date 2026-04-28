#Create a frequency array of numbers (count occurrence of each number).
n = int(input("Enter number of elements: "))

arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

# Find maximum element to decide size of frequency array
max_val = arr[0]
for i in range(1, n):
    if arr[i] > max_val:
        max_val = arr[i]

# Create frequency array
freq = [0] * (max_val + 1)

# Count occurrences
for i in range(n):
    freq[arr[i]] += 1

print("Frequency of elements:")
for i in range(len(freq)):
    if freq[i] != 0:
        print(i, "occurs", freq[i], "times")
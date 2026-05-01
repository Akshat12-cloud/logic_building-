#Create a frequency array of numbers (count occurrence of each number). 
def frequency_array(arr, max_value):
    # Create frequency array of size max_value + 1
    freq = [0] * (max_value + 1)

    # Count occurrences
    for i in range(len(arr)):
        freq[arr[i]] += 1

    return freq


# Example
arr = [1, 2, 3, 2, 4, 1, 2, 5, 3]
max_value = max(arr)

result = frequency_array(arr, max_value)

# Print frequencies
for i in range(len(result)):
    if result[i] > 0:
        print(f"{i} occurs {result[i]} times")
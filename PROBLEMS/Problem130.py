#Count how many pairs of elements have a sum equal to a given number k. 
def count_pairs(arr, k):
    count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                count += 1
                
    return count


# Example
arr = [1, 5, 7, 1]
k = 6
print(count_pairs(arr, k))
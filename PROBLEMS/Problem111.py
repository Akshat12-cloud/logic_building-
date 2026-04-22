#Compare two arrays — check if they contain the same elements (ignore order).
def are_equal(arr1, arr2):
    # If lengths are different → not equal
    if len(arr1) != len(arr2):
        return False

    n = len(arr1)

    for i in range(n):
        count1 = 0
        count2 = 0

        # Count occurrences in arr1
        for j in range(n):
            if arr1[i] == arr1[j]:
                count1 += 1

        # Count occurrences in arr2
        for j in range(n):
            if arr1[i] == arr2[j]:
                count2 += 1

        # If counts are different → arrays not equal
        if count1 != count2:
            return False

    return True


# Example
arr1 = [1, 2, 3, 2]
arr2 = [2, 1, 2, 3]

if are_equal(arr1, arr2):
    print("Arrays contain same elements")
else:
    print("Arrays are different")
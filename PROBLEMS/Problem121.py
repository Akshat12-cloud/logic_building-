#Find element-wise product of two arrays.
def element_wise_product(arr1, arr2):
    # Check if both arrays have same length
    if len(arr1) != len(arr2):
        print("Arrays must be of same length")
        return
    
    result = []
    
    # Multiply corresponding elements
    for i in range(len(arr1)):
        result.append(arr1[i] * arr2[i])
    
    return result


# Example
A = [2, 4, 6, 8]
B = [1, 3, 5, 7]

product = element_wise_product(A, B)
print("Element-wise product:", product)
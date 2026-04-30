#Find element-wise product of two arrays. 
# Function to calculate element-wise product
def element_wise_product(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Arrays must have the same length")
        return None
    
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] * arr2[i])
    
    return result


# Example arrays
A = [2, 4, 6, 8]
B = [1, 3, 5, 7]

# Function call
output = element_wise_product(A, B)

if output is not None:
    print("Element-wise product:", output)
#Find the index of the minimum element. 
def find_min_index(num):
    minimum = num[0]
    index = 0
    
    for i in range(len(num)):
        if num[i] < minimum:
            minimum = num[i]
            index = i
            
    return index

num = [5, 90, 495, 32, 21, 44, 69]
result = find_min_index(num)

print("The minimum element is at index", result)
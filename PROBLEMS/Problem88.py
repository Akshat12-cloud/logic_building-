#Find the index of the maximum element. 
      
def find_max_index(num):
    maximum = num[0]
    index = 0
    
    for i in range(len(num)):
        if num[i] > maximum:
            maximum = num[i]
            index = i
            
    return index

num = [5, 90, 495, 32, 21, 44, 69]
result = find_max_index(num)

print("The maximum element is at index", result)
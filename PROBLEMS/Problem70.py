# Print pattern of characters (A, AB, ABC, ...) recursively. 
def pattern(n, current=1):
    if current > n:
        return
    
    # Print characters from A up to current
    for i in range(current):
        print(chr(65 + i), end="")
    print()
    
    pattern(n, current + 1)

n = int(input("Enter number of rows: "))
pattern(n)
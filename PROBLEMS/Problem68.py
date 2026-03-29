#Print numbers in increasing and decreasing 
# order in same function.
def order(n):
    if n == 0:
        return
    print(n, end=" ")      # Decreasing order
    order(n - 1)
    print(n, end=" ")      # Increasing order

n = int(input("Enter a number: "))
order(n)
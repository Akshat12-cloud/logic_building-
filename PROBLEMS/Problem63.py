#Print a line of n stars recursively.
def pattern(n):
    for i in range(1,n+1):
        print("*", end="")
n=int(input("enter the number of stars:"))
pattern(n)


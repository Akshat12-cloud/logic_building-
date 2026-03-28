#Print a square of stars recursively (n×n). 
def pattern(n):
        for j in range(1,n+1):
            print("*"*n,end="")
            print()
            
n=int(input("enter the number of stars for length and breadth: "))
pattern(n)          
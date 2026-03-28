#Print a triangle of stars recursively (bottom-up). 
def pattern(n):
    if n==0:
        return
    pattern(n-1)
    print("*"*n)
n=int(input("enter the number of stars in the base:"))
pattern(n)
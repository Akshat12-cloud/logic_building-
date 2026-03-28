#Print a triangle of stars recursively (top-down).
def pattern(n):
    for i in range(1,n+1):
        if n>0: 
            print("*"*n)
        n-=1
n=int(input("enter the number of stars in the base:  "))
pattern(n)         
#Take n elements and print only those greater than a given value k.
def print_greater_than(num):
    for i in range(0,len(num)):
        if num[i]>k:
            print(num[i])
num=[78,67,26,88,96,45,21,44]
k=int(input("enter the number"))
results=print_greater_than(num)
print(f"the numbers greater than {k} is {results}")            
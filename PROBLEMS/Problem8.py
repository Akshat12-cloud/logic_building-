 #Check whether a number is a perfect square (without using the square root function).
num=int(input("enter the number: "))
i=1
while i*i<=num:
    if i*i==num:
        print(f"{num} is a perfect square")
        break
    i+=1
else:
    print(f"{num} is not a perfect square")
    



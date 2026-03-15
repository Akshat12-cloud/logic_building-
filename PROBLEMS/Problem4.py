#Check whether a given integer is single-digit, double-digit, or multi-digit.
num = int(input("Enter an integer: "))
num_abs = abs(num)

if num_abs < 10:
    print("Single-digit number")
elif num_abs < 100:
    print("Double-digit number")
else:
    print("Multi-digit number")

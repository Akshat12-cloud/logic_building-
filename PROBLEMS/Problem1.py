#Take a 3-digit number and check if all digits are distinct.
num = input("Enter a 3-digit number: ")


if len(num) == 3 and num.isdigit():

    digits = set(num)
    
    if len(digits) == 3:
        print("All digits are distinct.")
    else:
        print("Digits are not distinct.")
else:
    print("Invalid input. Please enter a 3-digit number.")

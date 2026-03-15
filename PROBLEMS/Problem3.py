#Take a 4-digit number and check if the first and last digits are equal.
num = input("Enter a 4-digit number: ")

if len(num) == 4 and num.isdigit():
    if num[0] == num[3]:
        print("First and last digits are equal.")
    else:
        print("First and last digits are not equal.")
else:
    print("Invalid input. Please enter a 4-digit number.")

#Take three numbers and check if they can form a Pythagorean triplet
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

nums = [a, b, c]
nums.sort()

if nums[0]**2 + nums[1]**2 == nums[2]**2:
    print("It is a Pythagorean triplet")
else:
    print("Not a Pythagorean triplet")
'''Take a password string and check basic rules (length ≥ 8 and contains at least one 
digit).'''

password = input("Enter your password: ")

if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Valid password")
else:
    print("Invalid password")


# Password Validator

# Get user input for the password
password = input("Enter a password: ")

# Validate the password based on the criteria
length = len(password) >= 8
upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
special = any(char in "!@#$%^&*()_+" for char in password)

# Check if all criteria are met
if length and upper and lower and digit and special:
    print("Password is strong.")
else:
    print("Password is weak.")

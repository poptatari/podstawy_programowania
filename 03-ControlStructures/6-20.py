###
# Program that converts a decimal number into a binary number.
#

# Ask the user to enter a decimal number
number = int(input("Enter decimal number: "))

# Store the original number for the final output
decimal = number

# Create an empty string to store the binary number
binary = ""

# Repeat the conversion process until the quotient becomes 0
while number > 0:

    # Calculate the remainder after dividing by 2
    remainder = number % 2

    # Add the remainder to the beginning of the binary string
    binary = str(remainder) + binary

    # Divide the number by 2 and keep only the integer quotient
    number = number // 2

# Print the original decimal number and its binary equivalent
print(f"{decimal}(10) = {binary}(2)")
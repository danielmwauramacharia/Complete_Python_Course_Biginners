# This code has the common format specifiers
# They are used to control how variables are formatted
# and printed together with strings
name = "John"
age = 30
height = 1.75
percentage = 0.75
integer_value = 42

# Format as a string
print(f"Name: {name:s}")

# Format as a decimal integer
print(f"Age: {age:d}")

# Format as a floating-point number
print(f"Height: {height:f}")

# Format as a floating-point number with 2 digits after the decimal point
print(f"Height (2 decimal places): {height:.2f}")

# Format as a hexadecimal integer (lowercase)
print(f"Integer value (hex lowercase): {integer_value:x}")

# Format as a hexadecimal integer (uppercase)
print(f"Integer value (hex uppercase): {integer_value:X}")

# Format as a binary integer
print(f"Integer value (binary): {integer_value:b}")

# Format as an octal integer
print(f"Integer value (octal): {integer_value:o}")

# Format as a percentage (multiplies by 100 and adds a % sign)
print(f"Percentage: {percentage:.0%}")

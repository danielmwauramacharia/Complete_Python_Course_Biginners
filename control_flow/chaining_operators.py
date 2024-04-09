# check for retirement age
# Eligibility from 18 to 65 years
age = input("Age: ")
valid_age = int(age)
"""
# Normal way of execution 
if valid_age >= 18 and valid_age <= 65:
    if valid_age == 65:
        print("you are on your retirement year")
    else:
        print(f"you have {65 - valid_age} years to work")
"""
if 18 <= valid_age <= 65:  # chaining operators
    if valid_age == 65:
        print("you are on your retirement year")
    else:
        print(f"you have {65 - valid_age} years to work")
else:
    print("Your age is outside working bracket")

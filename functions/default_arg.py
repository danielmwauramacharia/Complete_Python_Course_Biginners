# Having default arguments in python functions
# The default arguments should come after required ones
def increment(number, by=2):
    return number + by


print(increment(6, 3))  # default arg used

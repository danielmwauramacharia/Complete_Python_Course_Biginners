# This are loops that doesnt terminate
# The condition is always true
# They need loop control to exit from the loop
x = 1
while x > 0:
    print(x)
    x *= 3
    if x == 27:
        break  # loop control

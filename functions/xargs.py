# multiple arguments on function calling
def mult(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(mult(2, 3, 4, 5))

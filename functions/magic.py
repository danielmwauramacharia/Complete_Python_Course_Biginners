def magic_calculation(a, b, c):
    if a < b:
        return c
    if c < b:
        return a + b
    result = a * b
    result -= c
    return result


print(magic_calculation(4, 3, 5))

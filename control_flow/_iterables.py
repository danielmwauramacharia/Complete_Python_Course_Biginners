# Looking at the object type returned by range
# Iterables can also work with string , lists
# custom objects can also be iterable
for i in range(5):
    print(i)
print(type(range(5)))  # class range
for x in "python":  # iterate via string
    print(x)

# There are local and global variables
# Local variables are local to a function
# Global can be accessed anywhere in the program
# Global variables should be used with care
x = 10  # global
y = 5


def _sum():
    x = 3  # local to function
    y = 4
    return x + y


print(_sum())  # local values used
_add = x + y  # global values used
print(_add)

# Function that perform a task case 1
# function that return a value case 2

# case 1
def greet(name):
    print(f"Hi {name}")


greet("daniel")

# case 2


def get_greet(name):
    return f"Hi {name}"


message = get_greet("daniel")
print(f"The return message is: {message} ")

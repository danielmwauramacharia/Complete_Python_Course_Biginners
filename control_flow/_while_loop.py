# while loop in python
# Executes as long as the condition is true
num = 100
while num > 0:
    print(num)
    num //= 10
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

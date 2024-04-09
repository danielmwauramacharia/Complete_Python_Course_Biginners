# The fizz buzz algorithm
# prints fizz if divisible by 3
# prints buzz if divisible by 5
# prints fizz buzz if divisible by 3 and 5
# Return input if not divisible by 3 and 5

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("FizzBuzz")
    elif input % 3 == 0 and input % 5 != 0:
        print("Fizz")
    elif input % 5 == 0 and input % 3 != 0:
        print("Buzz")
    else:
        print(input)


num = input("Enter positive integer: ")
fizz_buzz(int(num))

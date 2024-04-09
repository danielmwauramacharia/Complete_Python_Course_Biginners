# The fizz buzz algorithm
# prints fizz if divisible by 3
# prints buzz if divisible by 5
# prints fizz buzz if divisible by 3 and 5
# Return input if not divisible by 3 and 5

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    else:
        print(num)


number = input("Enter positive integer: ")
fizz_buzz(int(number))

# for...else loop in python
success = False
for number in range(3):
    print("Attempt")
    if success:
        print("success")
        break
else:
    print("Tried 3 times unsuccesfully")

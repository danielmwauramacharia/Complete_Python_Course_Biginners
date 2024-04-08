# learning control flow by a loan program
salary = input("Enter salary per month: ")
student = input("Enter 1 if student or 0 otherwise:")
if int(student) == 1:
    print("loan not for students")
else:
    credit_score = input("what is your score: p, f , g , vg, e: ")
    if credit_score.lower() == "e":
        print(f"loan limit is: {int(salary) * 3}")
    elif credit_score.lower() == "g" or credit_score.lower == "vg":
        print(f"loan limit is: {int(salary) * 2}")
    else:
        print("Not Eligible")
print("**********Thank you**********")

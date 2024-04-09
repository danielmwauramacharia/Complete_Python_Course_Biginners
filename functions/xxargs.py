# passing multiple keyword arguments in function
# the data is stored as dictionaries
def info_user(**user):
    print(user)


info_user(id=1, name="daniel", age=26)

# for i in range(0, 100):
#     if i < 10:
#         print(f"0{i}, ", end='')
#     else:
#         print(f"{i}, " if i != 99 else f"{i}", end='')
for i in range(100):
    if i < 10:
        print("0{}, ".format(i), end='')
    else:
        print("{}, ".format(i) if i != 99 else "{}{}".format(i, "\n"), end='')

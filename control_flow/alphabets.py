# print alphabets in lowercase
# use string format in printing
for i in range(97, 123):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    print("{}".format(chr(i)), end='')

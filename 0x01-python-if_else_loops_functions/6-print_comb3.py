#!/usr/bin/python3
# Prints all possible different combination of two digits
for i in range(10):
    for j in range(1, 10):
        if (i != j and i < j):
            print("{}{}".format(i, j), end="")
            if i != 8:
                print(", ", end="")
            else:
                print()

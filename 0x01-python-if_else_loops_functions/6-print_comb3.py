#!/usr/bin/python3
i = 0
j = 1

for i in range(0, 8):
    for j in range(1, 10):
        if i < j:
            print("{}".format(i), end="")
            print("{}".format(j), end=", ")

print("{}".format(89))

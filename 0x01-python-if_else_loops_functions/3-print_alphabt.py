#!/usr/bin/python3
alpha = "abcdefghijklmnopqrstuvwxyz"

for a in alpha:
    if a == "e" or a == "q":
        continue
    print("{}".format(a), end="")

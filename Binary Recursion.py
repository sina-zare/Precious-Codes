def binary(x):
    if x == 0:
        return
    else:
        binary(int(x / 2))
        print(x % 2, end="")

y = binary(24)

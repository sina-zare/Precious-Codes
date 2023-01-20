def EasterEggs(total, basket1, basket2):
    if (basket1 + basket2) == total:
        print("Candy Time")
    else:
        print("Keep Hunting")


EasterEggs(int(input()), int(input()), int(input()))

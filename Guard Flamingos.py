def GuardFlamingos(length, width):
    perimeter= 2 * (length + width)
    flamingos= perimeter // 2
    return flamingos

print(GuardFlamingos(int(input()), int(input())))



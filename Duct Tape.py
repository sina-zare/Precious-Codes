# 1 foot= 12 inch
# 1 roll= 60 feet long & 2 inch wide
AreaOfOneRoll= 720 * 2

def area(x, y):
    return (((x*12) * (y*12)) * 2)
area= area(int(input()), int(input()))
check=( area // AreaOfOneRoll)

if (area % AreaOfOneRoll) > 0:
    print((check + 1))
else:
    print(check)


one = int(input())
two = int(input())
three = int(input())
four = int(input())
five = int(input())
six = int(input())

list = [one, two, three, four, five, six]
result = []

for i in list:
    if int(i / 3) == i / 3:
        result.append("Pop")
    elif int(i / 3) != i / 3 and int(i / 2) == i / 2:
        result.append("Crackle")
    elif int(i / 3) != i / 3 and int(i / 2) != i / 2:
        result.append("Snap")

print(" ".join(result))
lenght = int(input())
list = []
sum = 0

for i in range(lenght):
    list.append(int(input()))

for i in list:
    if (i % 2) == 0:
        sum += i

print(sum)
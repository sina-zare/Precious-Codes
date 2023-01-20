items = input().split(",")
aim = input()
time = 5
for i in items:
    if i == aim:
        print(time)
    else:
        time += 5
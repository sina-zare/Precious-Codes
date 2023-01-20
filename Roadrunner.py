X = int(input())
RRSpeed = int(input())
CSpeed = int(input())

for i in range(1, 1001):
    RoadRunner = X - (RRSpeed * i)
    Cayote = (X + 50) - (CSpeed * i)

    if RoadRunner <= 0:
        print("Meep Meep")
        break
    elif Cayote <= RoadRunner:
        print("Yum")
        break

SnackPoints= {"Lettuce": 5, "Carrot": 4, "Mango": 9, "Cheeseburger": 0}
SnackList= ["Lettuce", "Carrot", "Mango", "Cheeseburger"]

inp= input().split(" ")
TotalPoints= 0
for i in inp:
    if i in SnackList:
        TotalPoints += SnackPoints.get(i)
    else:
        continue
if TotalPoints >= 10:
    print("Come on Down!")
else:
    print("Time to wait")

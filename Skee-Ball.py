#every 12 point= 1 ticket, we wanna buy squirt gun
#score and squirtgun price(ticket) given as input
points= int(input())
cost= int(input())

tickets= int((points // 12))
if tickets >= cost:
    print("Buy it!")
else:
    print("Try again")
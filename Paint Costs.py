#canvas & brush= 40$ each color 5$
#money needed based on number of colors and tax is 10%

colors= int(input())
icost= (40 + (5 * colors))
fcost= icost + (icost * 0.1)
if int(fcost) == float(fcost):
    print(int(fcost))
else:
    print(int(fcost) + 1)


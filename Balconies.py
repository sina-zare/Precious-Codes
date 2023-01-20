# we have rectangle balconies
ap1= input().split(",")
ap2= input().split(",")

AreaAp1= int(ap1[0]) * int(ap1[1])
AreaAp2= int(ap2[0]) * int(ap2[1])

if AreaAp1 > AreaAp2:
    print("Apartment A")
else:
    print("Apartment B")
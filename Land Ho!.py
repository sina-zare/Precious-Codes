def LandHo(people):
    if people > 20:
        return ((((people//20)*10))*2+10)
    else:
        return 10


print(LandHo(int(input())))
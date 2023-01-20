def GothamCity(criminal):
    if criminal < 5:
        print("I got this!")
    elif criminal >= 5 and criminal <= 10:
        print("Help me Batman")
    else:
        print("Good Luck out there!")


GothamCity(int(input()))

AnimalNoise= {"Grr": "Lion", "Rawr": "Tiger", "Ssss": "Snake", "Chirp": "Bird"}
AnimalList= ["Grr", "Rawr", "Ssss", "Chirp"]

inp= input().split(" ")

for i in inp:
    if i in AnimalList:
        print(f"{AnimalNoise.get(i)} ")
    else:
        continue

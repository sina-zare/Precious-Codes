n= int(input())
out= list(range(1,n))

for i in out:
    if not (i % 2) == 0:
        if (i % 3) == 0 and (i % 5) == 0:
            print("SoloLearn")
        elif (i % 3) == 0:
            print("Solo")
        elif (i % 5) == 0:
            print("Learn")
        else:
            print(i)
    else:
        continue



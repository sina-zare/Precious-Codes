def EuroToDollar(euro):
    dollar =  float(euro) * 1.1
    return dollar


items = input()
list = items.split(" ")

flag = 0

for i in list:
    if EuroToDollar(i) > 20:
        print("Back to the store")
        break
    else:
        flag += 1

if flag == len(list):
    print("On to the terminal")


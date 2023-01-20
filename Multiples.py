#Multiples

def multiples(intg):
    sum = 0
    case = []
    for i in range(intg-1, 0, -1):
        case.append(i)
        for j in case:
            if j % 3 == 0:
                sum += j
            elif j % 5 == 0:
                sum += j

        return sum

try:
    print(multiples(int(input())))

except :
    print("number only!")
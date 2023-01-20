# 1 Peso = 2 Cent
# 50 Peso = 1 Dollar
# 100 Peso = 2 Dollar
# 1000 Peso = 20 Dollar

def PesoToDollar(x):
    return x / 50

pesos= int(input())
dollars= int(input())

if PesoToDollar(pesos) > dollars:
    print("Dollars")
else:
    print("Pesos")



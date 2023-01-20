def VowelCounter(string):
    StandardString = string.lower()
    A = StandardString.count("a")
    E = StandardString.count("e")
    I = StandardString.count("i")
    O = StandardString.count("o")
    U = StandardString.count("u")
    print(A + E + I + O + U)

VowelCounter(input())
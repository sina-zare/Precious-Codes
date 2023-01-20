def NumberOfOnes(x):
    binary = bin(x)
    print(binary.count("1"))

NumberOfOnes(int(input()))

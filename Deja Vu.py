inp = input()
letters = []
flag = 0
#asdasdasdl
for i in range(0 ,len(inp)):
    x = inp[i:i+1]
    letters.append(x)


for i in range(0, len(inp)):
    for j in range(0, len(inp)):
        if letters[i] == letters[j]:
            flag += 1

if flag > len(inp):
    print("Deja Vu")
else:
    print("Unique")
inp= list(input())
rev= []
for i in range((len(inp)-1), -1, -1):
    rev.append(inp[i])
print(" ".join(rev))
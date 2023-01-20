kaleido= int(input())

if kaleido > 1:
    cost= (kaleido * 5) - ((kaleido * 5) * 0.1)
else:
    cost= (kaleido * 5)
TotalPrice= cost + (cost * 0.07)
print(round(TotalPrice, 2))


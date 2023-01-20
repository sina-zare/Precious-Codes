#x >= 20 no tax
price = input()
price_list = price.split(",")
sum = 0

for i in price_list:
    if float(i) < 20:
        sum += (float(i) + (float(i) * 0.07))
    else:
        sum += float(i)

print(round(sum, 2))

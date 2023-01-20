def max_list(list):
    max_list = 0
    for i in range(len(list)):
        if max_list >= float(list[i]):
            continue
        else:
            max_list = float(list[i])
    return max_list


x = input()
list = x.split(",")
max_list = max_list(list)

proccessable_list = []
for i in list:
    proccessable_list.append(float(i))



top_of_list_price = max_list

cheap_list = []
for i in proccessable_list:
    cheap_list.append(i)
cheap_list.remove(max_list)

sum_of_other = 0
for i in cheap_list:
    sum_of_other += i

other_of_list_price = sum_of_other - (sum_of_other * 0.30)

sum_of_all = 0
for i in proccessable_list:
    sum_of_all += i

total_price_normal = sum_of_all + (sum_of_all * 0.07)
total_price_discount = top_of_list_price + other_of_list_price
total_price_discount_tax = total_price_discount + (total_price_discount * 0.07)
difference = total_price_normal - total_price_discount

save = total_price_normal - total_price_discount_tax

print(int(save))




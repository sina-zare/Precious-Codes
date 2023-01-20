x = input()
list = []
deny_list = [
            "!", "@", "#", "$", "%", "^",
             "&", "*", "(", ")", "-", "_",
             "=", "+", "`", "~", "/", ",",
             "<", ">", "?", ":", ";", "."
            ]
for i in x:
    list.append(i)

for i in range(1, len(x)):
    for j in list:
        if j in deny_list:
            list.remove(j)

print("".join(list))

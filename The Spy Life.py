x = input()
list = []
deny_list = [
            "!", "@", "#", "$", "%", "^",
             "&", "*", "(", ")", "-", "_",
             "=", "+", "`", "~", "1", "2",
             "3", "4", "5", "6", "7", "8",
             "9", "0", "/", ",", "<", ">",
             "?", ":", ";", "."
            ]

for i in x:
    list.insert(0, i)

#n Time Check
for z in range(1, len(x)):
    for j in list:
        if j in deny_list:
          list.remove(j)

print("".join(list))

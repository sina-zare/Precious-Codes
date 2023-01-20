group_members = input()
my_name = input()

group_list = group_members.split(" ")
flag = 0

for i in group_list:
    if i[0] == my_name[0]:
        print("Compare Notes")
        break
    else:
        flag += 1

if flag == len(group_list):
    print("No Such Luck")
    
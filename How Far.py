input = input()
'''
list_start = input.split("H")
P_list = []
for i in list_start:
    if "P" in i:
        P_list.append(i)

block_str = "".join(P_list)

semi_final_list = block_str.split("P")
blocks = semi_final_list[0].count("B")

print(blocks)
'''
left_B_strip = input.lstrip("B")
right_B_strip = left_B_strip.rstrip("B")
pure_format = right_B_strip
flag = 0
for i in pure_format:
    if i == "B":
        flag += 1

print(flag)


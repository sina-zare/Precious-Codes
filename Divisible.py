input_1 = int(input())
input_2 = input()
flag = 0

test_numbers = input_2.split(" ")
for i in test_numbers:
    if (input_1 % int(i)) == 0:
        flag += 1

if flag == len(test_numbers):
    print("divisible by all")
else:
    print("not divisible by all")

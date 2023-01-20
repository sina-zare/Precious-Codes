blue = int(input())
red = int(input())
green = int(input())
yellow = int(input())

leftover_blue = blue % 15
leftover_red = red % 15
leftover_green = green % 15
leftover_yellow = yellow % 15

total_leftover = leftover_blue + leftover_red + leftover_green + leftover_yellow

print(total_leftover)
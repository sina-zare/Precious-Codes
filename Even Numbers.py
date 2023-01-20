input = input()

list_of_numbers = input.split(" ")
even_numbers = []

for i in list_of_numbers:
    if ((int(i)  % 2) == 0):
        even_numbers.append(i)
even = " ".join(even_numbers)

print(even)

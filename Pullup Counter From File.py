x = open(r"C:\Users\Sina\Desktop\test2.txt", "r")
contents = x.read().splitlines()
x.close()
days = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pullup_dict = dict(zip(days, contents))

input = int(input("Enter Day: "))
print(f"Day {input}, {pullup_dict.get(input)} pull ups")

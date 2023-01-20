#Dictionary

MenuPrice= {"Nachos": 6, "Pizza": 6, "Cheeseburger": 10, "Water": 4, "Coke": 5}
MenuList= ["Nachos", "Pizza", "Cheeseburger", "Water", "Coke"]
Payment= 0
Order= input()
j= 0
for i in Order.split(" "):
    if (i in MenuList):
        Payment += MenuPrice.get(i)
    else:
        Payment += MenuPrice.get("Coke")
TotalPayment= Payment + ((Payment * 7) / 100)
print(TotalPayment)




#ba 3 ta az dustat miri football
#Nacho 6.00$  Pizza 6.00$ Cheeseburger 10$ Water 4.00$ Coke 5.00$ Tax 7%
Nachos= 6.00
Pizza= 6.00
Cheeseburger= 10.00
Water= 4.00
Coke= 5.00
Payment= 0.0

Order= input()
if "Nachos" in Order:
    Count= Order.count("Nachos")
    Payment += (Nachos * Count)
if "Pizza" in Order:
    Count = Order.count("Pizza")
    Payment += (Pizza * Count)
if "Cheeseburger" in Order:
    Count = Order.count("Cheeseburger")
    Payment += (Cheeseburger * Count)
if "Water" in Order:
    Count = Order.count("Water")
    Payment += (Water * Count)
if "Coke" in Order:
    Count = Order.count("Coke")
    Payment += (Coke * Count)

TotalPayment= Payment + ((Payment * 7) / 100)
print(TotalPayment)


#if ( ("Nachos" not in Order) and ("Pizza" not in Order) or ("Cheeseburger" not in Order) or ("Water" not in Order) or ("Coke" not in Order)):
#if Order[0:6] != "Nachos" and Order[0:5] != "Pizza" and Order[0:6] != "Cheese" and Order[0:5] != "Water" and Order[0:4] != "Coke":
#    Payment += Coke
#if Order[-6:-1] != "Nacho" and Order[-5:-1] != "Pizz" and Order[-6:-1] != "Chees" and Order[-5:-1] != "Wate" and Order[-4:-1] != "Cok":
#    Payment += Coke

########Calculation if bullshit word comes at 2nd word########
#if Order.index(" ") == 6:
#    #if first word was Nachos
#    if Order[7:14] != "Nachos" and Order[7:13] != "Pizza" and Order[7:19] != "Cheeseburger" and Order[7:13] != "Water" and Order[7:12] != "Coke":
#        Payment += Coke
#if Order.index(" ") == 5:
#    #if first word was Pizza or Water
 #   if Order[6:13] != "Nachos" and Order[6:12] != "Pizza" and Order[6:18] != "Cheeseburger" and Order[6:12] != "Water" and Order[6:11] != "Coke":
#        Payment += Coke
#if Order.index(" ") == 12:
#    #if first word was Cheeseburger
#    if Order[13:20] != "Nachos" and Order[13:19] != "Pizza" and Order[13:25] != "Cheeseburger" and Order[13:19] != "Water" and Order[13:18] != "Coke":
#        Payment += Coke
#if Order.index(" ") == 4:
#    #if first word was Coke
#    if Order[5:12] != "Nachos" and Order[5:11] != "Pizza" and Order[5:17] != "Cheeseburger" and Order[5:11] != "Water" and Order[5:10] != "Coke":
#        Payment += Coke




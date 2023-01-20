#mahi 10 ta Hovercraft misazi
#tedade moshterio dadan
#Hovercrafti 2,000,000$ pule sakhteshe ma mifrushim 3,000,000$
#mahi 1,000,000$ pule bime midim

#check kon aya sud kardi? age har mah vazife dashti 10 ta HC besazi, va tedade HC haye darkhasti ro tu input behet bedan.
# 21,000,000$ outgoing per month

Cost_Per_Month= 21000000
while 1==1:
    hovercraft= 3000000 * int(input("How many hovercrafts did you sell this month?  "))
    if hovercraft < Cost_Per_Month:
        print("Loss")
    elif hovercraft == Cost_Per_Month:
        print("Broke Even")
    else:
        print("Profit")


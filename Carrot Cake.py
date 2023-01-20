carrots = int(input())
boxes = int(input())

remainder = carrots % boxes
if remainder >= 7:
    print("Cake Time")
else:
    print(f"I need to buy {7 - remainder} more")


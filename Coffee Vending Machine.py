coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
    for i in range(5):
        if coffee[choice] == coffee[i]:
            print(f"{coffee[i]}")

except:
    print("Invalid number")

finally:
    print("Have a good day")

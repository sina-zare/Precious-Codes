#  MM/DD/YYYY to DD/MM/YYYY

def us_to_eu_date(us):
    dict = {
        "January": "1", "February": "2", "March": "3", "April": "4",
        "May": "5", "June": "6", "July": "7", "August": "8",
        "September": "9", "October": "10", "November": "11",
        "December": "12"
    }
    if "," in us:
        list_a = us.split(" ", 1)
        list_b = list_a[1].split(", ")
        for i in list_b:
            list_a.append(i)
        list_a.remove(list_a[1])
        for i in dict:
            if i == list_a[0]:
                list_a[0] = dict[i]
        print(f"{list_a[1]}/{list_a[0]}/{list_a[2]}")
    else:
        list = us.split("/")
        print(f"{list[1]}/{list[0]}/{list[2]}")

us_to_eu_date(input())
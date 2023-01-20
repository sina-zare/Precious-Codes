import datetime

given_date = input()

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

dict = {
        "January": "1", "February": "2", "March": "3", "April": "4",
        "May": "5", "June": "6", "July": "7", "August": "8",
        "September": "9", "October": "10", "November": "11",
        "December": "12"
    }
#seperating full format date to 3 numbers representing Y M D
if "," in given_date:
    list_full = given_date.split(" ", 1)
    list_b = list_full[1].split(", ")
    for i in list_b:
        list_full.append(i)
    list_full.remove(list_full[1])
    for i in dict:
        if i == list_full[0]:
            list_full[0] = dict[i]

#date assignment from full format
    year_a = list_full[2]
    month_a = list_full[0]
    day_a = list_full[1]
#turn date to week number
    week_num = datetime.date(int(year_a), int(month_a), int(day_a)).weekday()

else:
    list = given_date.split("/")
    year_b = list[2]
    month_b = list[0]
    day_b = list[1]
#turn date to week number
    week_num = datetime.date(int(year_b), int(month_b), int(day_b)).weekday()

#turn week number to week day
print(week_days[week_num])

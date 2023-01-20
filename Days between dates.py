'''

given_date_1 = "August 15, 1979"
given_date_2 = "August 15, 2018"

year_1 = 0
year_2 = 0
month_1 = 0
month_2 = 0
day_1 = 0
day_2 = 0

dict = {
        "January": "1", "February": "2", "March": "3", "April": "4",
        "May": "5", "June": "6", "July": "7", "August": "8",
        "September": "9", "October": "10", "November": "11",
        "December": "12"
    }
#-------------turn first date to 3 items-------------------
if "," in given_date_1:
    list_full_1 = given_date_1.split(" ", 1)
    list_b_1 = list_full_1[1].split(", ")
    for i in list_b_1:
        list_full_1.append(i)
    list_full_1.remove(list_full_1[1])
    for i in dict:
        if i == list_full_1[0]:
            list_full_1[0] = dict[i]
#date assignment from full format
    year_1 = list_full_1[2]
    month_1 = list_full_1[0]
    day_1 = list_full_1[1]
#------------------------------------------------------------


#-------------turn second date to 3 items-------------------
if "," in given_date_2:
    list_full_2 = given_date_2.split(" ", 1)
    list_b_2 = list_full_2[1].split(", ")
    for i in list_b_2:
        list_full_2.append(i)
    list_full_2.remove(list_full_2[1])
    for i in dict:
        if i == list_full_2[0]:
            list_full_2[0] = dict[i]
#date assignment from full format
    year_2 = list_full_2[2]
    month_2 = list_full_2[0]
    day_2 = list_full_2[1]
#------------------------------------------------------------

final_year = int(year_2) - int(year_1)
final_month = int(month_2) - int(month_1)
final_day = int(day_2) - int(day_1)

print((final_year*365) + (final_month*30) + final_day)

'''
import re
from datetime import datetime

da = input()
de = input()
a = datetime.strptime(da, '%B %d, %Y').strftime('%d/%m/%Y')
b = datetime.strptime(de, '%B %d,  %Y').strftime('%d/%m/%Y')

aa = datetime.strptime(a,'%d/%m/%Y')
bb = datetime.strptime(b,'%d/%m/%Y')

diff = bb -aa
print(diff.days)
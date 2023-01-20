PM_dict = {
            "1": "13", "2": "14", "3": "15", "4": "16", "5": "17", "6": "18", "7": "19", "8": "20", "9": "21", "10": "22", "11": "23"
}
AM_dict = {
            "12": "00", "1": "01", "2": "02", "3": "03", "4": "04", "5": "05", "6": "06", "7": "07", "8": "08", "9": "09"
}

input = input()
time_list = input.split(" ")
time = time_list[0]
meridian = time_list[1]

hour_minute_list = time.split(":")

for i in PM_dict:
    if meridian == "PM" and hour_minute_list[0] == i:
        hour_minute_list[0] = PM_dict[i]

for i in AM_dict:
    if meridian == "AM" and hour_minute_list[0] == i:
        hour_minute_list[0] = AM_dict[i]

print(f"{hour_minute_list[0]}:{hour_minute_list[1]}")

'''

*second solution*
a, b = input().split(":")
if b[-2] == 'P': a = str((int(a)+12)%24)
print(f"{a.zfill(2)}:{b[:2]}")

'''
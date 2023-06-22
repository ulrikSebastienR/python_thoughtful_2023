import datetime

current = datetime.datetime.date(datetime.datetime.today())
dob = datetime.date(1982,6,29)

age = current - dob # age.days will give age in days
#print("your age in days", age.days)


#1: subtract months and years and days. not finished but logic is clear
if current.month >= dob.month and current.day >= dob.day:
    print(f"{current.year - dob.year} years, {current.month-dob.month} m, {current.day-dob.day} ")
elif current.month >=dob.month and current.day < dob.day:
    print(f"{current.year - dob.year} y, {current.month}")
else:
    print(f"{current.year-dob.year-1} y {current.month+12 - dob.month} m")

#method 2: count by leap years
leap = 0
for year in range(dob.year+1,current.year-1):
    if year%4 == 0:
        leap += 1


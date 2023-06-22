#age_calc.py

"""#take age from user
y = int(input("enter your year"))
m """

import datetime
#dob = datetime.date(1982, 6, 29) #40y11m22d on 20.6 answer exact by both
#dob = datetime.date(1984, 2, 9) # 39y4m11d on 20.6 answer is exact by method 2
#dob = datetime.date(1951, 1, 2) # 72y5m18d on 20.6 answer is exact by both 
#dob = datetime.date(1947, 7, 1) # 75y11m19d on 20.6 answer is exact by method 2
#dob = datetime.date(2017, 1, 17) # 6y5m3d on 20.6 answer is exact by method 2
dob = datetime.date(2019, 5, 5) # 4y1m15d on 20.6 answer is exact by method 2
toutdesuite = datetime.datetime.date(datetime.datetime.today())

lived_days = (toutdesuite - dob).days

#method 1: simple logic naive approach
y = lived_days//365.2425
days = lived_days%365.2425
m = days//30.437
#calculation of days is complicated and d = int(days%30.437+1) produces errors and is referred as another method
if toutdesuite.day < dob.day:
    if toutdesuite.month in [4,6,9,11]:
        d = toutdesuite.day + 31 - dob.day
    elif toutdesuite.month in [1,2,5,7,8,10,12]:
        d = toutdesuite.day + 30 - dob.day
    else:
        d = toutdesuite.day + 28 - dob.day # leaving the leap year currently
else:
    d = toutdesuite.day - dob.day
print(f"user has lived {y} years {m} months {d} days") 



import datetime

#take age from user one by one
#y = int(input("enter your year"))
#take full dob in one go
##print("enter your dob in yyyy mm dd format")
##u = list(map(int, input().split()))
##dob = datetime.date(u[0], u[1], u[2])



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



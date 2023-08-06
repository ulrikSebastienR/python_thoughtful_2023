#merge in dict.py
sen = "what is happiness vs dopamine"
import datetime

d1 = [number for number in range(1,8)]
d2 = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
day = dict(zip(d1,d2))
birthdays = []
years = [year for year in range(1982,2024)]

for y in range(1982, 2024):
    dob = datetime.date(y, 6,29)
    numberday = dob.isoweekday()
    humanday = day[numberday] #how carefully we avoided 7 if elses with a dictionary
    birthdays.append(humanday)

yearwise_birthday = dict(zip(birthdays,years))
#make a count method for dictionaries

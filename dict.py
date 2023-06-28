de = {k:v for k,v in enumerate(range(0,50,10))}
# merge two dictionaries
first = [char for char in "abcdefghi"]
second = [number for number in range(10)]
third = [number for number in range(100,200,10)]
#define via one liner list comprehension
dx = {k:v for k, v in zip(first, second)}

#define through for loop
d, d2 = {}, dict()
for k,v in zip(first, second):
    d[k] = v
for k,v in zip(third, second):
    d2[k] = v
    
# or define directly through mapping
d = dict(zip(first, second))
d1 = dict(zip(third, first))

#merge
z = {**d, **d1}
#merge without using ** #zip zips only keys, cant add dict.items or dict

# another example
import datetime

d10 = [number for number in range(1,8)]
d20 = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
day = dict(zip(d10,d20))
birthdays = []
years = [year for year in range(1982,2024)]

for y in range(1982, 2024):
    dob = datetime.date(y, 6,29)
    numberday = dob.isoweekday()
    humanday = day[numberday] #how carefully we avoided 7 if elses with a dictionary
    birthdays.append(humanday)

yearwise_birthday = dict(zip(years, birthdays))
#make a count method for dictionaries based on values #make a reverse method for dictionaries based on keys

#filter years when birthday fell on "mardi" and count them
i = 0
for k,v in yearwise_birthday.items():
    #i = 0 i would again be reset to zero with each loop iteration if you set i here inside the loop
    if v == "mardi":
        print(k, v)
        i += 1

#interchange keys and values
day1 = {}
for k, v in day.items():
    day1[v] = k

#append/add one more item to a dictionary, just define it
day1[8] = "chaque matin"
#extend a dictionary by more than one itme
day1[9] = "nouvelle jour"
day1[10] = "anniversarie"
#merge two dictionaries without **
for k, v in d1.items():
    d[k] = v

#sort keys and then return new dictionary
#separate out keys first
l = []
for key, value in day.items():
    l.append(key)
#since they are already sorted
l.reverse()
#separate out values now
lv = []
for key, value in day.items():
    lv.append(value)
#now merge these two
    dz = dict(zip(l, lv)) #but this is not reverse or sort as the keys are not matched with their respective values

#create a new dictionary from existing based on some filter
l = [temperature/10 for temperature in range(20,440,5)]
f = lambda c: c*9/5+32
all_f = list(map(f, l))
temp_corr = dict(zip(l,all_f))
extreme = {}
for k,v in temp_corr.items():
    if k<20 or k>42:
        extreme[k] = v
#or through function
def extreme_temp(d):
    for k,v in d.items():
        if k<20 or k>42:
            extreme[k] = v
    return extreme











    




import integer_operations

alphabets = [char for char in "abcdefghijklmnopqrstuvwxyz"]
numbers = [number for number in range(1,27)]
de = {k:v for k,v in enumerate(range(0,50,10))}
#append to dictionary
de.update({"aa":10000})
# merge two dictionaries
first = [char for char in "abcdefghi"]
second = [number for number in range(10)]
third = [number for number in range(100,200,10)]
#define via one liner list comprehension
dx = {k:v for k, v in zip(first, second)}
dv = {10:"a",51:"ab",30:"ba",40:"ca",5:"aca"}

class DictionariesLearning:
    "various common operations on dictionaries"
    def __init__(self,d=de):
        self.d = d
    def values_from_keys(self):
        "arrange following"
        d = integer_operations.fc.closest_sum_using_dict() #self.d is common to entire class while d here is local to this function in question only
        for k,v in d.items():
            if k == sorted(d.keys())[0]:
                first, second, third = d[k]
        return first, second, third
    def key_value_matching1(self):
        d = integer_operations.fc.closest_sum_using_dict()
        for k, v in d.items():
            if k == min(d.keys()):
                first,second,third = d[k]
        return first,second,third
    def sort_dictionary_by_keys(self):
        d,d1 = integer_operations.fc.closest_sum_using_dict(),{}
        for k,v in d.items():
            for k in sorted(d.keys()):
                d1.update({k:v})
        return d1
    def swap_keys_values(self):
        d1 = {}
        for k,v in self.d.items():
            d1.update({v:k})
        return d1          
    def sort_by_values(self):
        d1,d = {},{10:"a",51:"ab",30:"ba",40:"ca",5:"aca"}
        for key, value in d.items():
            for v in sorted(d.values()):
                if value == v:
                    d1.update({key:v})
##        for v in sorted(d.values()): #both the ways are correct and lead same output
##            for key,value in d.items():
##                if value == v:
##                    d1.update({key:v})
        return d1
    def reverse_keys(self, d=dx, d1={}):
        for k in list(reversed(sorted(d.keys()))):#match against k,v what you want to operate on
            for key, value in d.items():
                if k==key:
                    d1.update({k:value})
        return d1#list(reversed(sorted(d.keys())))
    def reverse_values(self,d=dx,d1={}):
        for v in list(reversed(sorted(d.values()))): #match against k,v what you is your focus on
            for key, value in d.items():
                if v==value:
                    d1.update({v:key})
        return d1        
dl = DictionariesLearning()

def repetitions_arrange_alphabetically(s):
    "filtering dictionaries based on key and values"
    global alphabets, numbers
    d, valuesof_s, arranged = {}, [], []
    lookuptable = dict(zip(alphabets, numbers))
    for char in s:
        for k, v in lookuptable.items():
            if char == k:
                d.update({char:v}) #this is not actually needed was added to learn dictionaries
                valuesof_s.append(v)
    valuesof_s.sort()
    for item in valuesof_s:
        for k,v in lookuptable.items():
            if item == v:
                arranged.append(k)
    answer = "".join(arranged)

def invert_dict(dx):
    "invert keys and values of a dictionary"
    xd = {}
    for k,v in dx.items():
        xd[v] = k
    return xd

def sort_d_by_values(dx):
    pass





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
#https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python?rq=1
#z1 = d|d1 #guess depends on python's version, not working currently
z2 = {k:v for chaque in (d,d1) for k,v in chaque.items()}
def dic_merge(dict1,dict2):
    y = dict2.copy()
    dict1.update(y)
    return dict1
z3 = dic_merge(d,d1)

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

sen = "simple mais génial, écrivez une critique plus tard"
l = [number for number in range(50,15,-5)]
words = sen.split()
d = dict(zip(l,words))
dt = {}
#invert
##for k,v in d.items():
##    dt.update({v:k})
#sort by keys
##for key in sorted(list(d.keys())):
##    for k,v in d.items():
##        if key == k:
##            dt.update({k:v})
#reverse sort by keys
##for key in reversed(sorted(d.keys())):
##    for k,v in d.items():
##        if key == k:
##            dt.update({k:v})
#sort by values
for value in sorted(list(d.values())):
    for k,v in d.items():
        if value == v:
            dt.update({k:v})









    




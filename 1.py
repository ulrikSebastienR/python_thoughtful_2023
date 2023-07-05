def combinations_making_5(n):
    l = [[]]*n #initialize an empty nested list with 5 inner lists
    for number in range(1,n):
        for i in range(n):
            l[i].append(number)
            l[i].append(n-number)
        continue
    return l



var1, var2 = "dick","moby"
f = {k:v for k,v in zip(var1, var2)}

#print calendar for a year
import datetime

start = datetime.date(1982,1,1)
end = datetime.date(1983, 1,1)
duration = (end-start).days


for day in range(start, end):
    print(day)
    break

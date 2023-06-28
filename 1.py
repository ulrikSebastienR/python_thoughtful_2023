
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

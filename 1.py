#doing item vs item1, using dictionaries and recursion to remove duplicates
s = "the unbearable weight of massive talent"
      
            
            

def sort_string_list_by_length(l = ["great", "bien", "toute suite", "maitenant", "cest la vie"]):
    d, sorteddict = dict(), {}
    for item in l:
        d[len(item)] = item
    sortedstring = sorted(list(d.keys()))
    for k, v in d.items():
        for i in range(len(sortedkeys)):
            pass
    
    return d


d,sortedd = {}, {}
for item in s.split():
    d[len(item)] = item
l = sorted(list(d.keys()))

for k,v in d.items():
    for i in range(len(l)):
        sortedd[l[i]] = v
    

  
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

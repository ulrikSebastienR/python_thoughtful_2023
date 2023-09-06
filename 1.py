s = "the unbearable weight of massive talent"

lofs = list(s)
lofs1 = list(s)
dups = {}
for item in s:
    i =0
    for item1 in s:
        if item == item1:
            i+=1
            dups.update({item:i})
for item in dups.keys():    
    for k,v in dups.items():
        if v>1:
            try:
                lofs.remove(item)
            except:
                pass
#doing item vs item1, using dictionaries and recursion to remove duplicates, for vs while loop for removing duplicates

for item in lofs1:
    i = 1
    while item.count!=1:
        try:
            lofs1.remove(item)
            i+=1
        except:
            pass
        
    
            
            
            

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

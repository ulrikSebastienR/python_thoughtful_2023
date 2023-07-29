#statement in like a normal loop 
l = [temperature/10 for temperature in range(20,440,5)]#range doesnt support floats
#lambda
f = lambda c: 9/5*c + 32
f2 = lambda x,y : x+y
f3 = lambda k,v : k>42 or k<20

#map
all_f = list(map(lambda c: c*9/5+32, l))
#temperature_correlation table
temp_corr = {k:v for k,v in zip(l,all_f)}
#filter
fever = list(filter(lambda t: t>37, l))
#difference between filter and without filter
#lambda for first squaring and then filtering the even squares
numbers = [number for number in range(20)]
sq = list(map(lambda n: n**2, numbers))
even_sq = list(map(lambda n:n%2==0, sq)) #list contains true false
even = list(filter(lambda n:n%2==0, sq)) #now list contains values like 4, 16

#https://stackoverflow.com/questions/72921131/lambda-in-nested-loop-with-condition
a = [[1,-2, 3, -4, 5, -6], [-10,22, -30, 41]]
#merge the lists and cube only positive values with lambda and without lambda
#check len(a)
a1, a2 = [i for i in a]
al = list(filter(lambda n:n**3, map(lambda n:n>0, a1+a2)))#output is list of booleans
al1 = list(map(lambda n:n**3, filter(lambda n:n>0, a1+a2)))#required output 

#INCOMPLETE filter/lambda to separate out values from a dict avec les keys
extreme = {}
for k, v in temp_corr.items():
    if k<20 or k>42:
        extreme[k] = v

ex = {}
def separate(d):
    for k, v in d.items():
        if k<20:
            ex[k] = v
    return ex


#low = dict(filter(separate, temp_corr)) 
#d = dict(map(f3, temp_corr.items()))


cel = [temp/10 for temp in range(30,440,10)]
faren = list(map(lambda x: x*9/5+32, cel))
lookup = dict(zip(cel, faren))


class ActualFunctions:
    def __init__(self, l=cel,d=lookup,s=""):
        "functions to be converted to one liners"
        self.l = l
        self.d = d
        self.s = s
    def filter_list_dict(self):
        l,z = [],{}
        for k,v in lookup.items():
            if k>38 or k<12:
                l.append(k)
                z.update({k:v})
        return l,z
af = ActualFunctions()

class OneLiners:
    def __init__(self,l=cel,d=lookup,s=""):
        "Learning various One Liners for the actual functions in class"
        self.l=l
        self.d=d
        #self.s=s
    def filter_list(self):
        "filter is to filter values in a list while map is to apply a lambda to all values in a list. Map will return a list of true false for each value if you use it for filtering"
        extreme = filter(lambda x: x>38 or x<12, cel)
        return list(extreme)
    def filter_dicts(self):
        """convert this
        z = {}
for k,v in lookup_temperature.items():
    if k>30:"""
        
       
ol = OneLiners()

l, z = [],{}
for k,v in lookup.items():
    if k>38 or k<12:
        l.append(k)
        z.update({k:v})

mf = list(filter(lambda k,v: dict(k,v) if k>38 else none, lookup.items()))

            



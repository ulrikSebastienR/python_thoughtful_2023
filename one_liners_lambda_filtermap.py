#statement in like a normal loop 
l = [temperature/10 for temperature in range(20,440,5)]#range doesnt support floats
#lambda
f = lambda c: 9/5*c + 32
f2 = lambda x,y : x+y
#f3 = lambda k,v : k>42 or k<20 not working

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

#required DS
cel = [temp/10 for temp in range(30,440,10)]
faren = list(map(lambda x: x*9/5+32, cel))
lookup = dict(zip(cel, faren))
#entered = [number for number in range(-10,10)]
number1,number2 = 15,25
farentocel = {k:v for k,v in zip(faren,cel)} #define dict by one liner
mess = {**lookup, **farentocel} #merge dictionaries by one liner

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
    def lcm(self,n1=number1,n2=number2): #not complete yet
        larger = n2 if n2>n1 else n1
        for number in range(larger,larger*1000):
            if n1*number == n2*number:
                lcm = number
                break            
        return larger#, lcm
    def hcf(self,n1 = number1, n2=number2):
        smaller = n2 if n2<n1 else n1
        for number in range(1,smaller+1):
            if n1%number==0 and n2%number==0:
                hcf = number
        return smaller, hcf
af = ActualFunctions()

class OneLiners:
    entered = [number for number in range(-10,10)]
    def __init__(self,l=cel,d=lookup,s=""):
        "first put your return value follwed by the condition but dont go complicating one liners too much so as to compromise the code readability"
        self.l=l
        self.d=d
        #self.s=s
    def if_else_single(self,entered=entered):
        y = list(map(lambda x: x if x>0 else x**2, entered))
        return y
    def if_else_multiple(self,entered=entered):
        "its better not to attempt confusing and unreadable one liners"
        y = list(map(lambda x:x**3 if 0<x<5 else x if x>5 else x**2, entered))
        return y
    def filter_list(self):
        "filter is to filter values in a list while map is to apply a lambda to all values in a list. Map will return a list of true false for each value if you use it for filtering"
        extreme = filter(lambda x: x>38 or x<12, cel)
        return list(extreme)
    def assignment(self,n=number1): #note a function can take as a paramter a variable outside of the class
        a,b,*c = [number for number in range(5)] #assigning a list together with other variables in one line
        c.append(n) # a function can have its own paramter other than instance or class variable
        return a, b, c
    def nested_for_loops(self):
        output = ['e', 'n', 't', 'r', 'o', 'p', 'y', 'v', 's', 'c', 'h', 'a', 'o', 's', 'z', 'e', 'b', 'r', 'a', 's', 'c', 'h', 'o', 'i', 's', 'i', 'r', 'p','a', 's']
        nested =  [item for item in (_*2 for _ in output)] #strings can be multiplied like numbers
        return nested
    def filter_dicts(self): #INCOMPLETE YET
        """convert this
        z = {}
for k,v in lookup_temperature.items():
    if k>30:"""           
ol = OneLiners()

class Examples_of_One_liners:
    "some common tasks done by one liners"    
    def __init__(self):
        pass
    def lcm_by_one_liner(self,n1=number1,n2=number2):
        larger = n2 if n2>n1 else n1
        multiples = [number for number in range(larger,larger*10000) if number%n1==number%n2==0]
        lcm = min(multiples)
        return larger, lcm, multiples
    def hcf(self,n1=number1,n2=number2):
        smaller = n2 if n2<n1 else n1
        hcf = max([number for number in range(1,smaller+1) if n1%number==0 and n2%number==0])
        return smaller, hcf
    def total(self):
        total = sum([number for number in range(10)])
        return total
    def multiples_de_deux_nombres(self):
        multiples_de_2_et_3 = [number for number in range(1000) if number%2==0 and number%3==0]
        return multiples_de_2_et_3
    def evenodd(self):
        evenodd = ["even" if number%2==0 else "odd" for number in range(20)]
        return evenodd
eol = Examples_of_One_liners()
    
l, z = [],{}
for k,v in lookup.items():
    if k>38 or k<12:
        l.append(k)
        z.update({k:v})



            



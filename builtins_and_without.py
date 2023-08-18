class WithoutUsingBuiltIns:
    "Emulating useful tasks without using built-in functions"
    def __init__(self, number=3, l=[number for number in range(1,5)]):
        self.l = l                                  
        self.number = number
    def permutations(self):
        "nested for loops must be run equal to number of items to pick, need to automate the process"
        perms,choose = [],self.number
        for first in self.l:
            for second in [number for number in self.l if number!=first]:
                for third in [number for number in self.l if number!=first and number!=second]:
                    perms.append((first,second,third))
        return perms, len(perms) #verified with itertools.permutations([1,2,3,4],3)
    def combinations(self):
        my_combs = self.permutations()[0]
        for item in my_combs:
            for item1 in [_ for _ in my_combs if _!= item]:
                if set(item)==set(item1):
                    my_combs.remove(item1)
        return my_combs        
##        #PREVIOUS INCOMPLETE ATTEMPT not working currently
##        combs_list, choose = [], self.number
##        for first in self.l:
##            for second in [number for number in self.l if number!=first]:
##                for third in [number for number in self.l if number!=first and number!=second]:                    
##                    combs_list.append((first,second,third))
##        return combs_list, len(combs_list) #set is unhashable type so a set cant filter if its components are set themselves
    def diff_two_ds(self,ds2=tuple(number for number in range(5)),ds1=tuple(number for number in range(3))):       
        diff = [item for item in ds1 if item not in ds2] #need to make it dynamic to automatically put first the bigger one
        return diff
    def power(self, raised):
        power = self.number
        for i in range(raised-1):
            power = power*self.number            
        return power
wubi = WithoutUsingBuiltIns()

class UsefulBuiltIns:
    "Useful builtin functions"
    def __init__(self, l = [_ for _ in range(30)], n=5):
        self.l = l
        self.n = n
    def use_of_enumerate(self):
        return list(enumerate(self.l)) #enumerate(l) will also work fine as a class can directly pickup outside variable    
    def characters_of_a_file_with_enumerate(self):
        f = open("openquestions.tex")
        for count, line in enumerate(f.read(),1):
            yield count, line
        f.close()
    def lines_of_a_file_with_enumerate(self):
        with open("openquestions.tex") as f:
            for count, line in enumerate(f,1):
                yield count,line    
            
ubi = UsefulBuiltIns()
#useful builtins
#sorted, reversed

#useful builtins in imports
#from itertools import permutations, combinations
        
    

#counting without len
l = [i for i in range(0,100,5)]
i = 0
for item in l:
    i += 1


#various sorting in python
#without using inbuilt function

#sort a list
l = [31, 23, 83, 12, 86, 97, 34, 18]
l1 = [31, 23, 83, 12, 86, 97, 34, 18]
l_s = []
while len(l)!=0:
    l_s.append(min(l))
    l.remove(min(l))

#sort a dict by keys

l2 = [char for char in "abcdefgh"]
d = dict((k,v) for k,v in zip(l1,l2))
keys = [i for i in d.keys()]
keys1 = [i for i in d.keys()]
l_keys = []
while len(keys1)!=0:
    l_keys.append(min(keys1))
    keys1.remove(min(keys1))
d = dict((k,v) for k,v in zip(l_keys,l2))  
    

#counting without len
l = [i for i in range(0,100,5)]
i = 0
for item in l:
    i += 1

from itertools import combinations, permutations
combs = list(combinations([number for number in range(5)],2))  
    

print(list(permutations([number for number in range(1,5)],3)))
print("combs",list(combinations([number for number in range(1,5)],3)))




      

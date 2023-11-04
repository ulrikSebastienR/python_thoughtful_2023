#operations common to tuples, lists and strings. Dictionary operations are in dict.py file though these operations can be applied to filter dictionaries based on keys and values
do = [[number for number in range(19,88,8)],[number for number in range(10) if number%2!=0],[number for number in range(33,55) if number%3==0],[number for number in range(10,20) if number%2==0]]
merged_do = [19, 27, 35, 43, 51, 59, 67, 75, 83, 1, 3, 5, 7, 9, 33, 36, 39, 42, 45, 48, 51, 54, 10, 12, 14, 16, 18]#could not do it with list comprehension
list_to_check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1]
s1,s2="audrey_bien","aurore_delplace"

class DSOperations:
    "common operations to lists, tuples and strings, enter your ds to operate on"
    def __init__(self, ds1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1],ds2=[number for number in range(4)], s="j dis oui madamoiselle cest arien neira madam oui"):
        self.ds1 = ds1
        self.ds2 = ds2
        self.s = s
        #self.s2 = s2
    def distance_between_strings(self, s1="audrey_bien",s2="aurore_delplace"):
        "make one string from another string, leetcode problem"
        total_characters = len(s1) if len(s1)>len(s2) else len(s2)
        distance = 0
        indices_unmatched = []
        for i in range(total_characters):
            try:
                if s1[i] != s2[i]:
                    distance += 1
                    indices_unmatched.append(i)
            except:
                pass
        return total_characters,distance, indices_unmatched
    def make_one_string_from_another(self,s1="audrey_bien",s2="aurore_delplace"):
        "leetcode problem"
        pass
    def sort_list_on_basis_of_another_list(self):
        "sort l1 on basis of l2"
        l1 = ["boy","girl", "enfant", "joun", "fille"]
        l2 = [5,2,51,32,12,29]
        d = dict(zip(l2,l1))
        sorted_l1 = []
        for key in sorted(d.keys()):
            for k,v in d.items():
                if k == key:
                    sorted_l1.append(v)                   
        return sorted_l1
    def all_sublists_using_combinations(self):
        "create sublists using permutations and combinations"
        from itertools import combinations
        sublists = []
        for i in range(1,len(self.ds2)):
            sublists.extend(combinations(self.ds2,i))
        return sublists
    def direct_all_sublists(self):
        sublists = []
        for i in range(len(self.ds1)+1):
            for j in range(1,len(self.ds1)+1):
                add = self.ds1[i:j]
                if j>=i and add!=[]:
                    sublists.append(add)
        return sublists
    def all_substrings_direct(self):
        substrings = []
        white_space_removed = "".join(self.s.split())
        for i in range(len(white_space_removed)+1):
            for j in range(1,len(white_space_removed)+1):
                add = white_space_removed[i:j]
                if j>=i and add != []: #includes blank sublists
                    substrings.append("".join(add))
        return substrings
    def bitwise_and_for_matching_two_ds(self):
        "using bitwise & operator to match two dss"        
        if len(self.ds1)==len(self.ds2) and set(self.ds1)&set(self.ds2):
            return "perfect Match"
        elif set(self.ds1) & set(self.ds2):        
            return set(self.ds1) & set(self.ds2)
        else:
            return "no match"
    def match_two_ds(self):
        "directly match two ds without inbuilts"
        diff = [element for element in self.ds1 if element not in self.ds2]
        if diff:
            return diff
        elif len(self.ds2)>len(self.ds1):
            return [element for element in self.ds2 if element not in self.ds1]
        else:
            return "perfect match"            
    def group_anagrams_and_repeats(self):#INCOMPLETE need to have one item only once
        "takes a string and groups anagrams but excludes repeats"
        anagrams, repeated = [],[]
        for substring in self.all_substrings_direct():
            for substring1 in [item for item in self.all_substrings_direct() if item!=substring]:
                if set(substring) == set(substring1) and substring != substring1:
                    anagrams.append(substring)
                elif substring == substring1:
                    repeated.append(substring)                
        return anagrams, repeated
    def anagrams_in_a_sentence_or_words(self):
        words = self.s.split()
        duplicates, anagrams = [],[]
        for word in words:
            for word1 in words:
                if set(word)==set(word1) and word!=word1:
                    anagrams.append(word)            
        return anagrams
    def duplicates_in_a_sentence_or_words(self):#INCOMPLETE, fais le plus tard
        words = self.s.split()
        duplicates = []
        for word in words:
            i = 0
            for word1 in words:
                pass
                
        return duplicates
    def duplicates_in_allsubstrings(self):
        "find duplicates"
        l,d = self.all_substrings_direct(), {}
        for substring in self.all_substrings_direct():
            i = 1
            for substring1 in self.all_substrings_direct():
                if substring == substring1:
                    i+=1
            if i>1:
                d.update({substring:i})
        return list(d.keys())
    def remove_duplicates_from_all_substrings(self):#INCOMPLETE, taking too long
        "find and remove duplicate substrings"
        without_duplicates = [item for item in self.all_substrings_direct() if item not in self.duplicates()]
        return without_duplicates
    def whitespaces_without_string(self):
        "strips all white spaces of a string"
        return "".join(self.s.split())             
    def set_inside_set(self):
        "though set can remove duplicates but what if your ds has all sets to checked for duplicates error thrown is unhashable type"
        return
    def duplicates_single_string(self,check="madamoiselle"):
        duplicates, duplicate_items = {},[]
        for item in self.s:
            i = 0
            for item1 in self.s:
                if item==item1:
                    i+=1
            if i>1:
                duplicates.update({item:i})
        for k,v in duplicates.items():
            if v>1:
                duplicate_items.append(k) #only duplicate items
        print(duplicates_items) #we would be modifying duplicates_items to reduce frequency of each item by 1 and then update the original string
        list_after_removing_one_duplicate = [] #PENDING
        for item in duplicates_items:#shallow vs deep copy, make a deep copy
            pass
        return duplicates, duplicate_items
    def reverse_a_string(self,to_reverse="the fireflies are all gone"): #sep 29 using inbuilt methods
        "reversed and sorted are python's inbuilt methods while sort and reverse are list in place methods"
        return "".join(item for item in list(reversed(to_reverse)))
    def sort_a_string(self, sep30 = "mindfulness activates frontal lobe"): #sep 30
        return "".join(item for item in sorted(sep30))
    def sort_using_ord(self, sep29 = "tango libre love of JC, domi et goon"): #INCOMPLETE
        "lists can be sorted using simple min or sorted function or ord too"
        l = [ord(char)-ord('0') for char in sep29]
        lsorted = [l[0]]
        for item in l:
            if item <= lsorted[-1]:
                lsorted.append(item)
                l.remove(item)
        return lsorted, l
       
        
dso = DSOperations()
dso1 = DSOperations([number for number in range(4,7)],[number for number in range(3)])

class Conversions:
    "converting one type of data to another"
    def __init__(self, n=12341234, l = [number for number in range(10)],s="1234"):
        self.n = n
        self.l = l
        self.s = s
    def number_to_list(self): #INCOMPLETE aout 12, 2023
        l, n = [], self.n
        i = 0
        while n%10!=0:
            l.append(n%10)
            n = n//10            
            i+=1
        #return l
        return "".join(str(item) for item in list(reversed(l)))
    def string_to_integer(self):
        #ord() works only on positive integer and takes strings only as input
        l = []
        for item in s:
            l.append(str(ord(item)-ord("0")))#to convert list to integer
        return int("".join(l))
    def list_to_integer1(self):
        "method 1 to convert list to integer"
        return int("".join(str(item) for item in self.l))
    def list_to_integer2(self):
        "method 2 to convert list to integer"
        pass
        
c = Conversions()
s = "1234"



for char in s:
    print(ord(char)-ord("0"))
    
l1, l2 = tuple([1,2]), tuple([3,4]) #+ operator works on list, string, tuple but not sets
l1 = l1+l2
print(l1+l2,l1,l2, type(l1+l2),type(l1)) #modified the string in place?
l1 = l1*4
print(l1, type(l1))

def only_one_duplicates(s="the unbearable weight of massive talent"):
    "only one occurence of a duplicate is removed, #sep7"
    lofs = list(s)
    for item in dups.keys():    
        for k,v in dups.items():
            if k==item and v>1: #lofs = [] if only v>1
                try:
                    lofs.remove(item)
                except:
                    pass
    return dictofduplicates(lofs)

def remove_all_duplicates_while(s="the unbearable weight of massive talent"):
    "so that each character/item appears only once"
    lofs1 = list(s)
    for item in lofs1:
        i = 0
        while (lofs1.count(item)!=1):
            i+=1    #provided counter at the starting of while loop to avoid confusion
            lofs1.remove(item)
    return dictofduplicates(lofs1)      
        
def dictofduplicates(s="the unbearable weight of massive talent"):
    "to verify if all the duplicates have been removed"
    dups = {} 
    for item in s:
        i=0
        for item1 in s:
            if item==item1:
                i+=1
        dups.update({item:i})
    return dups
        
def remove_all_duplicates_combined(s="the unbearable weight of massive talent"):               
    "combination of count duplicates and while loop, keep only one occurence of each character"
    dups = {}
    for item in s:
        i = 0
        for item1 in s:
            if item==item1:
                i+=1
        dups.update({item:i})
    if max(dups.values())==1:
        return "".join(char for char in dups.keys())
    else:
        allchars = list(dups.keys())
        for item in allchars:
            i = 0
            while (allchars.count(item)!=1):
                allchars.remove(item)
                i +=1
        return "".join(char for char in allchars)      


def recursion_to_remove_all_duplicates(s="the unbearable weight of massive talent"):
    "combination of count duplicates and delete one by one"#INCOMPLETE
    dups = {}
    for item in s:
        i = 0
        for item1 in s:
            if item==item1:
                i+=1
        dups.update({item:i})        
    if max(dups.values())==1:
        return "".join(char for char in dups.keys())
    else: 
        print(dups)
        allchars = list(dups.keys())
        print(allchars)
        #return f"{id(dups)}, {id(allchars)}"
        for item in allchars:#concurrent modification INCOMPLETE
            print(item)
            for k,v in dups.items():
                if item==k and v>1:
                    print(item)
                    allchars.remove(item)
        return recursion_to_remove_all_duplicates("".join(char for char in allchars))
##        #return dups

pour_duplicates = "the fireflies are all gone"
lpd = list(pour_duplicates)
for item in lpd:
    for item1 in lpd:
        pass
    




    

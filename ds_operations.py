#operations common to tuples, lists and strings. Dictionary operations are in dict.py file though these operations can be applied to filter dictionaries based on keys and values
do = [[number for number in range(19,88,8)],[number for number in range(10) if number%2!=0],[number for number in range(33,55) if number%3==0],[number for number in range(10,20) if number%2==0]]
merged_do = [19, 27, 35, 43, 51, 59, 67, 75, 83, 1, 3, 5, 7, 9, 33, 36, 39, 42, 45, 48, 51, 54, 10, 12, 14, 16, 18]#could not do it with list comprehension
list_to_check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1]

class DSOperations:
    "common operations to lists, tuples and strings, enter your ds to operate on"
    def __init__(self, ds1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1],ds2=[number for number in range(4)], s="j dis oui madamoiselle cest arien neira madam oui"):
        self.ds1 = ds1
        self.ds2 = ds2
        self.s = s
        #self.s2 = s2
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
   
        
dso = DSOperations()
dso1 = DSOperations([number for number in range(4,7)],[number for number in range(3)])
       

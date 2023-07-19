class ListOperations:
    def __init__(self,l1=[_ for _ in range(10)],l2=[_ for _ in range(5)]):
        self.l1 = l1
        self.l2 = l2
    def subtract_l2_from_l1(self):
        diff = [item for item in self.l1 if item not in self.l2]
        return diff
lo = ListOperations()

class StringOperations:
    "make it a class that has common operations on strings other classes will refernce methods from this class"
    def __init__(self,s="hope is a fancy word"):
        self.s = s
    def subtract_strings(self,s1):
        diff = "".join([_ for _ in list(self.s) if _ not in list(s1)]) #s1 is to be input by the user or come from outside the class
        return diff
    def subtract(self, s1): #access another class method 
        diff = ListOperations(list(self.s),list(s1)).subtract_l2_from_l1()
        return "".join(diff)
so = StringOperations()

class LongestSubstringWithNoRepetitions:
    "Find longest substring of a string that has no repetiting characters"
    def __init__(self, s="Happiness is getting bored of doing your wish. Dopamine is chasing garbage to satisfy pleasure hormone site in your brain"):
        self.s = s
    def list_of_duplicates(self,to_check): #every instance method needs to have self otherwise it wont run
        duplicates = set() #to check s, use lsnr.method_name(lsnr.s)
        for item in to_check:
            i = 0
            for item1 in to_check:
                if item == item1:
                    i+=1
            if i>1:
                duplicates.add(item)
        return list(duplicates)
    def frequencies(self):
        freq = {}
        for char in self.s:
            i = 0
            for char1 in self.s:
                if char == char1:
                    i+=1
            freq.update({char:i})
        return freq
    def duplicates(self):
        duplicates = {}
        for k,v in self.frequencies().items():
            if v>1:
                duplicates.update({k:v})
        return duplicates
    def indices(self):
        "indices of first repeating alphabet"
        indices = []
        item = list(self.duplicates())[0]
        for i in range(len(self.s)):
            if self.s[i] == item:
                indices.append(i)                
        return indices
    def all_indices(self):
        "indices of all alphabets getting repeated"
        indices = {}      
        l = list(self.duplicates().keys())
        for alphabet in l:
            item_indices = []                
            for i in range(len(self.s)):
                if self.s[i] == alphabet:
                    item_indices.append(i)
            indices.update({alphabet:item_indices})           
        return indices
    def manual_split_substrings(self):
        substrings = []
        return substrings
    def substrings_using_rsplit(self):
        "split using rsplit"
        substrings = []
        for char in list(self.duplicates().keys()):
            substrings.extend(self.s.rsplit(char))
        return substrings
    def duplicates_substrings(self):
        "substrings may contain duplicates"
        duplicates_substrings = []
        for string in self.substrings_using_rsplit():
            count = 0
            for string1 in self.substrings_using_rsplit():
                if string == string1:
                    count += 1
            if count>1:
                duplicates_substrings.append(string)
        return duplicates_substrings
    def arrange_strings_by_length(self):
        d,length_wise = {}, {} 
        for string in self.substrings_using_rsplit():
            d.update({string: len(string)}) #strings with same length will be removed if you do d.update({len(string):string})
        for value in list(reversed(sorted(d.values()))):
            for k,v in d.items():
                if v == value:
                    length_wise.update({k:value})
        return list(length_wise)
    def longest_substring(self):
        d = {}
        for string in self.arrange_strings_by_length():
            if self.list_of_duplicates(string) == []:
                return string
            #d.update({string:self.list_of_duplicates(string)}) #output verified with storing strings and their duplicates in a dictionary
            #break #break destoyed the program needs to be checked
        #return d

lsnr = LongestSubstringWithNoRepetitions()



string="Happiness is getting bored of doing your wish. Dopamine is chasing garbage to satisfy pleasure hormone site in your brain"
d, length_wise = {}, {}
def has_duplicates(s=string):
    #global string
    for char in s:
        i = 0
        for char1 in s:
            if char1 == char:
                i+=1
        if i>1:
            #d.update({char:i})
            return True
            break
        #return False
    return "vedika bahl"
        
      



 

             
        


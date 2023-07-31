#from browse_file_dirs import FileOperations

#reverse a string, you can reverse a list using l.reverse()
s = "madamoiselle"
alphabets = [char for char in "abcdefghijklmnopqrstuvwxyz"]
numbers = [number for number in range(1,27)]

class StringOperations:
    "various operations on string"
    def __init__(self,s="madamoiselle"):
        self.s = s
    def has_repetitions(self):
        "finds if string has any character repeated"
        d = {}
        for char in self.s:
            if s.count(char)>1:
                d.update({char:s.count(char)})
        return d
    def freq_of_each_character(self):
        "without str.count method finds repeated characters in string"
        d = {}
        for char in self.s:
            i = 0
            for char1 in self.s:
                if char == char1:
                    i+=1
            d.update({char:i})        
        return d
    def prefix_find(self, s1="freedom", s2="free", s3="freemankind", s4="freaking"):
        "find longest prefix in the given strings"
        pre = []
        smallest = min(len(s1),len(s2), len(s3), len(s3))
        for i in range(smallest):
            if s1[i] == s2[i] == s3[i] == s4[i]:
                pre.append(s1[i])
            else:
                break            
        return "".join(pre), smallest
    def print_zigzag_pattern(self):
        s1 = "i  i \n a m \n   m \n g  \n   a \n   r      ima      \n indian         chef \n"
        print(s1)
    def merge_zigzag_pattern_from_file(self,s1):                
        pass
    def find_zigzag_pattern(self,s1):
        pass    
    def reverse_string(s):
        l = [char for char in s]
        l_reversed = []
        l_reversed.extend(l[len(l)-1-i] for i in range(len(l)))
        return "".join(l_reversed)
    def reverse_string2(self):
        "cant reverse a string using reversed(s)"
        l = []
        for i in range(len(self.s)-1,-1,-1): #-1 end point of range because if you put 0, range will not take first alphabet as 0 wont be included
            l.append(s[i])
            return "".join(l)        
    def arrange_alphabetically_no_repetition(s):
        "arrange a string or list alphabetically without repetitions"
        global alphabets, numbers
        lookuptable = dict(zip(alphabets, numbers))
        d, ans, v_arranged = {}, {}, []
        for char in s:
            for k,v in lookuptable.items():
                if char == k:
                    d.update({char:v})
                    v_arranged.append(v)
        v_arranged.sort()
        for item in v_arranged:
            for k,v in d.items():
                if item == v:
                    ans.update({k:item})
        answer = "".join(list(ans))
            
        return d, v_arranged, answer
    def repetitions_arrange_alphabetically(s):
        "arrange a list or string alphabetically with repetitions allowed"
        global alphabets, numbers
        d, valuesof_s, arranged = {}, [], []
        lookuptable = dict(zip(alphabets, numbers))
        for char in s:
            for k, v in lookuptable.items():
                if char == k:
                    d.update({char:v}) #this is not actually needed was added to learn dictionaries
                    valuesof_s.append(v)
        valuesof_s.sort()
        for item in valuesof_s:
            for k,v in lookuptable.items():
                if item == v:
                    arranged.append(k)
        answer = "".join(arranged)        
        return d, valuesof_s,arranged, answer
so = StringOperations()        
                    



#join

sen = "happiness is feeling so full that you get bored. dopamine is chasing after noise"
print(sen.split())
print("+".join(sen))

# string is immutable
words = sen.split()

class ListOperations:
    def __init__(self,l1=[_ for _ in range(10)],l2=[_ for _ in range(5)]):
        self.l1 = l1
        self.l2 = l2
    def subtract_l2_from_l1(self):
        diff = [item for item in self.l1 if item not in self.l2]
        return diff
lo = ListOperations()

class StringOperations1:
    "make it a class that has common operations on strings other classes will refernce methods from this class"
    def __init__(self,s="hope is a fancy word"):
        self.s = s
    def subtract_strings(self,s1):
        diff = "".join([_ for _ in list(self.s) if _ not in list(s1)]) #s1 is to be input by the user or come from outside the class
        return diff
    def subtract(self, s1): #access another class method 
        diff = ListOperations(list(self.s),list(s1)).subtract_l2_from_l1()
        return "".join(diff)
so1 = StringOperations1()

class LongestSubstringWithNoRepetitions:
    "Find longest substring of a string that has no repetiting characters"
    def __init__(self, s="Happiness is getting bored of doing your wish. Dopamine is chasing garbage to satisfy pleasure hormone site in your brain"):
        self.s = s
    def list_of_duplicates(self,to_check): #every instance method needs to have self otherwise it wont run
        "this method is equivalent to self.duplicates().keys()"
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
    def split_substrings(self): #s.split("t") and s.rsplit("t") are same
        substrings = []
        for char in self.list_of_duplicates(lsnr.s):            
            substrings.extend(self.s.split(char)) #note use of extend merges all the lists together
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








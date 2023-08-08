#in all list methods, you can not do l= l.remove(i) as l will be none type now
# Program examples are at the end of this file
#make multiple lists in one go
l = [[].append(char) for char in "abcde"] #wont work as [] is a none type
l1 = [[char] for char in "abcde"] #works
l2 = [[0]]*5 #works however all sublists would point to the same object or false lists
l3 = [[]] *5 #works however python treats all these blank lists differently IS PENDING
do = [[number for number in range(19,88,8)],[number for number in range(10) if number%2!=0],[number for number in range(33,55) if number%3==0],[number for number in range(10,20) if number%2==0]]
merged_do = [19, 27, 35, 43, 51, 59, 67, 75, 83, 1, 3, 5, 7, 9, 33, 36, 39, 42, 45, 48, 51, 54, 10, 12, 14, 16, 18]#could not do it with list comprehension
list_to_check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1]

class ListOperations:
    "useful list operations"
    def __init__(self, l=list_to_check):
        self.l = l
    def find_indices(self):
        pass
    def duplicates(self,entered="chaque matin"):
        duplicates = []
        for item in entered:
            i = 0
            for item1 in entered:
                if item == item1:
                    i+=1
            if i>1:
                duplicates.append(item)
        return duplicates            
    def in_place_modification_et_remove_duplicates(self, entered=[]):
        s = "bonjour"
        l = list(s)
        duplicates = self.duplicates(s)
        l[:] = [item for item in l if item not in duplicates] #note using l[:]
        return l       
    def merge_lists(self):
        m = []
        do=[[number for number in range(19,88,8)],[number for number in range(10) if number%2!=0],[number for number in range(33,55) if number%3==0],[number for number in range(10,20) if number%2==0]]
        for sublist in do:
            m.extend(element for element in sublist)
        return do, m 
    def sort_without_sorted(self):
        l = self.merge_lists()[1]
        lsorted = [l[0]]
        for i in range(self.count_element_including_subelements_in_sublists()):
            try:
                for item in l:
                    if item<lsorted[-1]:
                        lsorted[-1]=item
                l = [item for item in l if item not in lsorted]
                lsorted.append(l[0])
            except:
                pass
        return i,lsorted, len(lsorted), l
    def match_or_subtract_two_lists(self):
        "matches smaller list against bigger to find which element are missing from bigger"
        bigger = [number for number in range(10)]# lo.merge_lists()[1]
        smaller = [number for number in range(5)] #lo.sort_without_sorted()[1]
        #return bigger, len(bigger), smaller, len(smaller) to check lists in current comparison
        leftouts = [element for element in bigger if element not in smaller]
        return leftouts        
    def count_element_including_subelements_in_sublists(self):
        do = self.merge_lists()[0]
        i = 0
        for sublist in do:
            for element in sublist:
                i += 1
        return i
    def remove_all_duplicates(self):
        "do in place, make a set and then convert set to list"
        l = [[number for number in range(20) if number%2==0]]
        return l
    def merge_sublists_element_wise(self): 
        merge = []
        to_traverse = max(len(item) for item in do)
        for i in range(to_traverse):
            for j in range(len(do)):
                try:
                    merge.append(do[j][i])
                except:
                    pass
        return merge
    def sort_without_sorted_using_while(self):
        l = self.merge_lists()[1]
        lsorted = [l[0]]
        i=0
        while i!= self.count_element_including_subelements_in_sublists()-1:
            #for i in range(self.count_element_including_subelements_in_sublists()):
            try:
                for item in l:
                    if item<lsorted[-1]:
                        lsorted[-1]=item
                l = [item for item in l if item not in lsorted]
                lsorted.append(l[0])
            except:
                pass
            i+=1
        return i,lsorted, len(lsorted), l
    def all_sublists(self):
        "find all sublists or substrings or subtuples"
        sublists = []
        for i in range(len(self.l)):
            for j in range(len(self.l)):
                if j>i:
                    sublists.append(self.l[i:j])
        return sublists
    def arrange_sublists_length_wise_nested_for(self):
        "arrange sublists length wise using nested for loop"
        arranged, sublists = [],[]
        for i in range(len(self.l)):
            for j in range(len(self.l)):
                if j>i:
                    sublists.append(self.l[i:j])
        for i in range(len(self.l)):#no need to subtract one as range itself subtracts 1
            for item in sublists:
                if len(item) == i:#nested for
                    arranged.append(item)
        return arranged
    def arrange_sublists_length_wise_dict(self):
        sublists, d = self.all_sublists(), {}
        for item in sublists:
            d.update({tuple(item):len(item)}) #lists are unhashable type in python so only strings or tuples can be used as keys to a dict
        return d
    def incomplete_merge_sublists_element_wise(self): #earlier attempts UNDER OBSERVATION
        len_to_traverse, merged, merged1, automatic = max(len(item) for item in do), [], [], []
        #method 1 not automatic        
        for i in range(len_to_traverse):
            try:
                merged.append(do[0][i]) #make this automatic
                merged.append(do[1][i])
                merged.append(do[2][i])
                merged.append(do[3][i])
            except: #[19, 1, 33, 10, 27, 3, 36, 12, 35, 5, 39, 14, 43, 7, 42, 16, 51, 9, 45, 18, 59, 67, 75, 83]
                pass #leaves elements from middle range sublists after all elements from smallest sublists are done
        #method 2 trying automatic 
        for j in range(len(do)):
            for i in range(len_to_traverse):
                try:
                    automatic.append(do[j][i])
                except:
                    pass        #[19, 27, 35, 43, 51, 59, 67, 75, 83, 1, 3, 5, 7, 9, 33, 36, 39, 42, 45, 48, 51, 54, 10, 12, 14, 16, 18]
        for i in range(len_to_traverse):
            for j in range(len(do)):
                try:
                    merged1.append(do[j][i])
                    merged1.append(do[j][i])
                    merged1.append(do[j][i])
                    merged1.append(do[j][i]) #[19, 19, 19, 19, 1, 1, 1, 1, 33, 33, 33, 33, 10, 10, 10, 10, 27, 27, 27, 27, 3, 3, 3, 3, 36, 36, 36, 36, 12, 12, 12, 12, 35, 35, 35, 35, 5, 5, 5, 5, 39, 39, 39, 39, 14, 14, 14, 14, 43, 43, 43, 43, 7, 7, 7, 7, 42, 42, 42, 42, 16, 16, 16, 16, 51, 51, 51, 51, 9, 9, 9, 9, 45, 45, 45, 45, 18, 18, 18, 18, 59, 59, 59, 59, 48, 48, 48, 48, 67, 67, 67, 67, 51, 51, 51, 51, 75, 75, 75, 75, 54, 54, 54, 54, 83, 83, 83, 83], 
                except:
                    pass
        return merged, merged1, automatic
lo = ListOperations()

class RemoveEmptySublists:
    "empty lists are false objects so cant be removed by l.remove"
    def __init__(self, l=[[char] for char in "abcdefghi"], digits= [number for number in range(int(7/2+1))]):
        self.l = l
        self.digits = digits  #from make7 or combinations making a number program
        for i in range(len(self.digits)): #you can run a code in class definiton if a code is common to the class
            self.l[i].append(self.digits[i])#note this and next line since this is class definition so self.l and l are interchangable
            l[i].append(7-self.digits[i]) #note this and previous line
        for sublist in self.l:
            sublist.pop(0)      

    def correct_method(self):
        self.l = [sublist for sublist in self.l if sublist !=0]
        return self.l #[[0, 7], [1, 6], [2, 5], [3, 4]]
    
    def correct2(self):
        self.l = [sublist for sublist in self.l if sublist]
        return self.l #[[0, 7], [1, 6], [2, 5], [3, 4]]
    
    def wrong_method(self):
        for sublist in self.l:
            if sublist == []:
                self.l.remove(sublist)
        return self.l #[[0, 7], [1, 6], [2, 5], [3, 4], [], []]

    def wrong2(self):
        for i in range(len(self.digits)): #we need it here separately but need to comment out same code in class definition otherwise same code would run twice
            self.l[i].append(self.digits[i])
            self.l[i].append(7-self.digits[i])
##        for sublist in self.l:
##            sublist.pop(0)
##            if sublist == []:
##                self.l.remove(sublist)             
        return self.l
z = RemoveEmptySublists()    
    
    
    

s = "madamoiselle"
alphabets = [char for char in "abcdefghijklmnopqrstuvwxyz"]
numbers = [number for number in range(1,27)]
                    
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

def list_methods():
    "list methods"
    l = [[char, 1,5,6,5,6] for char in "abcde"]
    for sublist in l:
        sublist.pop(0) #pops item at the index provided, default 0
        sublist.remove(5) #removes first appearance of the value
    return l
    

#convert list to dictionary
def list_to_dict(l):
    d = dict(enumerate(l))
    return d
#making a nested list
list_nested = [[1]]*6

#extend in lists
a = [[1,-2,3,-4],[-10,21,-32,40]]
a1, a2 = [i for i in a]
a1.extend(i for i in a2)
#making new reversed list by extend or you can do l.reverse
l_string = [char for char in "madamoiselle"]
lreversed = []
lreversed.extend(l_string[len(l_string)-1-i] for i in range(len(l_string)))


#l1 = l2
numbers = [i for i in range(20)]
even = [i for i in range(20) if i%2 == 0]

#subtract
odd = [i for i in numbers if i not in even]
#see if a list is subset of another list
x = all(even) in numbers #outputs True if x is subset of numbers

# merge to make exactly identical to original list
new_numbers = []
for i, j in zip(even, odd):
    new_numbers.append(i)
    new_numbers.append(j)

#do numbers + even but exclude the repeating
merged_repeated = numbers + even

for i in merged_repeated:
    if merged_repeated.count(i) > 1:
       merged_repeated.remove(i)

l1 = [char for char in "abcdefghijklmn"]
l2 = [char for char in "0123456789"]
#INTENDED OUTPUT = "aBcDe" DONE



l = []
i = len(l1) if len(l1) < len(l2) else len(l2)
for j in range(i):
    l.append(l1[j] if j%2 == 0 else l2[j])

#INTENDED OUTPUT = a0b1c2--i9jklmn DONE

l_extended = []
i_big = len(l1) if len(l1)>len(l2) else len(l2)

for j in range(i_big):
    if j < i:
        l_extended.append(l1[j])
        l_extended.append(l2[j])
    else:
        l_extended.append(l1[j])
    

#INTENDED OUTPUT = a9b8 DONE
l_mixed = []        
for j in range(i):
    l_mixed.append(l1[j] if j%2==0 else l2[i-j])

#INTENDED OUTPUT = a9b8j0klmn DONE
l_rev = []
for j in range(i_big):
    if j < i:
            l_rev.append(l1[j])
            l_rev.append(l2[i-1-j])
    else:
            l_rev.append(l1[j])
	


#INTENDED OUTPUT = a9b8--i0nmlkj
l_1rev = []

for j in range(i_big):
    if j < i:
        l_1rev.append(l1[j])
        l_1rev.append(l2[i-1-j])  
for k in range(i_big-i):
    l_1rev.append(l1[i_big-1-k])
   
#look at difference in output of these two programs
def program1(n):
    for i in range(5):
        l = [char for char in "abcde"]
        l.remove(l[i])
        #print(l[i])
    return l

def program2(n):
    for i in range(5):
        l = [char for char in "abcde"]
        print(l[i])
        l.remove(l[i])
    return l

for j in range(len(l)-1, 0,  -1):
    print(l[j])

l1 = [number for number in range(5)]
l2 = [char for char in "abcde"]
d = dict(zip(l1,l2))
l3 = [char for char in "abcd"]
d3 = dict(zip(l1,l3))


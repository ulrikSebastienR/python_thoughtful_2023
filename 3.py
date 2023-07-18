l = ["madamoiselle", "distract", "and"]
sorted_list = [""]
for item in l:
    if len(item)>= len(sorted_list[-1]):
        sorted_list.append(item)

numbers = [11,21,3,16,81,92,29]
ns = min(numbers)
for item in numbers:
    if item > 1:
        pass

s1 = "mascho piro in manu national park, peru"
l1 = []
for i in range(len(s1)):
    if s1[i] == "p":
        l1.append(i)
        
    


#to do
def exponent_recursion(number, power):
    if power == 1:
        return number
    else:
        return exponent_recursion(number, power-1)
    
def sort_string_alphabetically(s):
    "sorts a string alphabetically"
    l = [char for char in "abcdefghijklmnopqrstuvwxyz"]
    d = dict(enumerate(l,1))
    position_of_s = []
    for char in s:
        for k,v in d.items():
            if char == v:
                position_of_s.append(k)
    position_of_s.sort()
    return s_sorted

def duplicates_in_string(s):
    "finds duplicates in a string"
    l = [char for char in "abcdefghijklmnopqrstuvwxyz"]
    d = dict(enumerate(l,1))
    position_of_s = []
    for char in s:
        for k,v in d.items():
            if char == v:
                position_of_s.append(k)
    position_of_s.sort()
    return duplicates

def duplicates_using_freq(s):
    pass

l = [char for char in "abcdefghijklmnopqrstuvwxyz"]
d = dict(enumerate(l,1))
s = "distraction"
position_of_s = []
for _ in s:
    for k,v in d.items():
        if _ == v:
            position_of_s.append(k)
position_of_s.sort()
    
    

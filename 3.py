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
    

l = [char for char in "abcdefghijklmnopqrstuvwxyz"]
d = dict(enumerate(l,1))
s = "distraction"
position_of_s = []
for _ in s:
    for k,v in d.items():
        if _ == v:
            position_of_s.append(k)
position_of_s.sort()
    
    

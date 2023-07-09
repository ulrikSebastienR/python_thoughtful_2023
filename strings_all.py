#reverse a string, you can reverse a list using l.reverse()
s = "madamoiselle"
alphabets = [char for char in "abcdefghijklmnopqrstuvwxyz"]
numbers = [number for number in range(1,27)]

def reverse_string(s):
    l = [char for char in s]
    l_reversed = []
    l_reversed.extend(l[len(l)-1-i] for i in range(len(l)))
    return "".join(l_reversed)
                      
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

#join

sen = "happiness is feeling so full that you get bored. dopamine is chasing after noise"
print(sen.split())
print("+".join(sen))

# string is immutable
words = sen.split()





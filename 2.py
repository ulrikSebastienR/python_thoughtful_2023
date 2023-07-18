class StringOperations:
    def __init__(self,s = "the unforgettable lightness of being"):
        self.s = s
    def repeated(self):
        repeats = set()
        for char in s:
            if s.count(char)>1:
                repeated.add(char)
        return repeats
    def repetitions(s="madamoiselle"):
        "checks if string has any repeated characters"
        d = {}
        for char in s:
            if s.count(char) >1:
                d.update({char:s.count(char)})
        return d        

x = StringOperations()

def indices_of_repeating_chars(s="the unforgettable weight of massive talent"):
    repeats = set()
    for char in s:
        if s.count(char)>1:
            repeats.add(char)
    d = {}
    for element in repeats:
        s.index(element)
        d.update({element: s.rfind(element)}
        #return d

def longest_substring(s="the unforgettable weight of massive talent"):
    repeats = set()
    for char in s:
        if s.count(char)>1:
            repeats.add(char)
    l = []
    for element in repeats:
        l.extend(item for item in s.rsplit(element))
    #now sort list by length of strings
    
            
    return repeats, l

def sort_list_by_lengths_of_elements(l=['', '', '', '', ' massive talent', ' of massive ', ' tal', ' unforg', ' w', 'able weigh', 'alen', 'ble weight of m', 'e unforgettable weig', 'e weight of massive ta', 'ent', 'ettable wei', 'f massive talent', 'forgettable weight of massive tale', 'ght of mass', 'he unforge', 'ht of massive talent', 'ight of massiv', 'ive talent', 'lent', 'massive', 'nt', 'of', 'orgettable weight o', 'rgettable weight ', 'ssive t', 't', 't', 't of massive talent', 'talent', 'th', 'the', 'the u', 'the un', 'the unf', 'the unfor', 'the unforgett', 'the unforgettab', 'the unforgettable we', 'the unforgettable weight of ma', 'ttabl', 'unforgettable', 've talent', 'weight']):
    sorted_list = [l[0]]
    for item in l:
        if len(item) >= len(sorted_list[-1]):
            sorted_list.append(item)
    return sorted_list

l = ['', '', '', '', ' massive talent', ' of massive ', ' tal', ' unforg', ' w', 'able weigh', 'alen', 'ble weight of m', 'e unforgettable weig', 'e weight of massive ta', 'ent', 'ettable wei', 'f massive talent', 'forgettable weight of massive tale', 'ght of mass', 'he unforge', 'ht of massive talent', 'ight of massiv', 'ive talent', 'lent', 'massive', 'nt', 'of', 'orgettable weight o', 'rgettable weight ', 'ssive t', 't', 't', 't of massive talent', 'talent', 'th', 'the', 'the u', 'the un', 'the unf', 'the unfor', 'the unforgett', 'the unforgettab', 'the unforgettable we', 'the unforgettable weight of ma', 'ttabl', 'unforgettable', 've talent', 'weight']


            
        

    


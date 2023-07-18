def count_dupl(user_input):
    "count duplicates and their occurence in strings or lists with order preserved"
    d = {}
    for char in user_input:
        i = 0
        for char1 in user_input:
            if char == char1:
                i+=1
        d.update({char:i})
    return d


def count_duplicates1(user_input):
    "counts frequencies of duplicates in strings, lists etc, output urordered"
    l = []
    for item in set(user_input):
        i = 0
        for item1 in user_input:
            if item == item1:
                i += 1
        l.append((item, i))
    return l

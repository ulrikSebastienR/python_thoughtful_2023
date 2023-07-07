def count_duplicates(user_input):
    "counts frequencies of duplicates in strings, lists etc"
    l = []
    for item in set(user_input):
        i = 0
        for item1 in user_input:
            if item == item1:
                i += 1
        l.append((item, i))
    return l

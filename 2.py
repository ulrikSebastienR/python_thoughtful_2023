#stuck at remove all blank sublists from a list
def pour_list():
    user_list = [number for number in range(7)]
    

def make7():
    n = 7
    digits = [number for number in range(int(n/2+1))]
    l = [[char] for char in "abcdefg"]

    for i in range(len(digits)):
        l[i].append(digits[i])
        l[i].append(n-digits[i])

    for sublist in l:
        sublist.pop(0)
    return l
    
def removeblanklists7():
    n = 7
    digits = [number for number in range(int(n/2+1))]
    l = [[char] for char in "abcdefg"]

    for i in range(len(digits)):
        l[i].append(digits[i])
        l[i].append(n-digits[i])

    for sublist in l:
        sublist.pop(0)
##        print(sublist)
##        if sublist == []:
##            print(l)
##            l.remove(sublist) #[[0, 7], [1, 6], [2, 5], [3, 4], ['f']]
##            print(l)
    """for sublist in l:
        if sublist == []:
            l.remove(sublist) #[[0, 7], [1, 6], [2, 5], [3, 4], []]"""
            

    return l

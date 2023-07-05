def make_5(n):
    "finds all combinations that when added make number 5 or n"
    l = [[]]*n
    
    for sublist in l:
        to_browse = [_ for _ in range(1,int(n/2)+1)]
        for number in to_browse:
            sublist.append(number)
            sublist.append(n-number)
            
            break
        to_browse.remove(number)
        #break
        
    return to_browse, l
        
            
            

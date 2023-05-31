l1 = [char for char in "abcdefghijklmn"]
l2 = [char for char in "0123456789"]

i = len(l1) if len(l1) < len(l2) else len(l2)
i_big = len(l1) if len(l1) > len(l2) else len(l1)
                     
                    
#intended a9b8c7i0nmlkj
l_1rev = []
for j in range(i_big):
    if j < i:
        l_1rev.append(l1[j])
        l_1rev.append(l2[i-1-j])
    else:
        l_1rev.append(l1[i_big-1-])
        


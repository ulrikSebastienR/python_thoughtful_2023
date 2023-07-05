l = [[]]*6
l1 = [char for char in "sandrine bonnaire"]
for char in l1:
    i = 0
    for char1 in l1:
        if char == char1:
            i += 1
            if i >1:
                print(char, i)


l2 = [1]*len(l1)
l = list(zip(l1,l2))

for k,v in l:
    for k1,v1 in l:
        if k==k1:
            v+=1

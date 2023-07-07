#intended output was to find combinations that can make 5 [[1,4],[2,3]]
#coudnt do with sublist nested for loops
#l = [[].append(char) for char in "abcde"] #wont work
n = 5
l = [[]]*int(n/2)
p = [[char] for char in "abcde"]
q = [[0]]*int(n/2)
r = [_ for _ in range(1,int(n/2+1))]
s = [char for char in "abcde"]


'''for number in r:
    for sublist in l:
        sublist.append(number)
        sublist.append(n-number) #output [['a', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1], ['b', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1], ['c', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1], ['d', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1], ['e', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1]]
        #r.remove(number) #[['a', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1], ['b', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1], ['c', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1], ['d', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1], ['e', 0, 5, 1, 4, 2, 3, 3, 2, 4, 1]] doesnt take value of r from inside loop
        #break # [['a', 0, 5, 2, 3, 4, 1], ['b'], ['c'], ['d'], ['e']] control never reaches beyond sublist 1 because of break
        #continue #[['a', 0, 5], ['b', 0, 5], ['c'], ['d'], ['e']]
    r.remove(number) #[['a', 0, 5, 2, 3, 4, 1], ['b', 0, 5, 2, 3, 4, 1], ['c', 0, 5, 2, 3, 4, 1], ['d', 0, 5, 2, 3, 4, 1], ['e', 0, 5, 2, 3, 4, 1]]'''
    
'''for number in r:
    print(r)
    r.append(number*10)
    print(r)
    r.remove(number)
    print(r) #loop can actually update from inside'''


d = dict(zip(r,s))
#append to dict 
d.update({"aa":1000})

for i in range(int(n/2)):
    p[i].append(r[i])
    p[i].append(n-r[i])
    q[i].append(r[i])
    q[i].append(n-r[i])
    l[i].append(r[i])
    l[i].append(n-r[i])
#output p = [['a', 1, 4], ['b', 2, 3], ['c'], ['d'], ['e']]
#output l = [[1, 4, 2, 3], [1, 4, 2, 3]]
#output q =  [[0, 1, 4, 2, 3], [0, 1, 4, 2, 3]]   
    
    



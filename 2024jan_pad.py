#max without using max function
#lcm array
#generate list containing random integers
#control b opens module browser in a program

import random

#lcm
def lcm_array(a=[2,3,4]):
    greater = max(a)    
    for i in range(greater, greater*1000):
        for item in a:
            if i%item !=0:
                break
        if item == a[-1]:
            return i

##l = []                
##def fibb(x=1,y=1):
##    y,x = x+y, y
##    return x,y
##for i in range(5):
##    l.append(fibb(x,y)[1])
        
l = []
l.extend(random.randint(1,50) for i in range(5))
        
        
    
        

#max
rl = [random.randint(1,90) for i in range(10)] #create a list
sl = [rl[0]]
for item in rl:
    if item > sl[-1]:
        sl.append(item)

#dict
t = (2,'a'),(3,'b')
d = dict(t)
    

    


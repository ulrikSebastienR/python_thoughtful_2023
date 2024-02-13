#INCOMPLETE sort a list without using sorted or sort function
#INCOMPLETE PROGRAMS ARE AT THE TOP
#LEARNT #control b opens module browser in a program

#max without using max function
#lcm array
#generate list containing random integers


import random

#fibb in a list
def fibb_series_in_a_list(terms=7):
    "will output one less term than entered"
    fibb_series = []    
    def lfibb(n):
        if n<=0:
            return "please enter positive numbers"
        elif n==1 or n==2:
            return 1
        else:
            return lfibb(n-1) + lfibb(n-2)

    for i in range(1,terms):
        fibb_series.append(lfibb(i))
    return fibb_series




    


#lambda, map and filter        
        

    
        
        
    
        

#max
rl = [random.randint(1,90) for i in range(10)] #create a list
sl = rl[0]
for item in rl:
    if item > sl:
        sl= item
print(sl, max(rl), rl)        

import os
print(os.getcwd())
os.chdir("/home/normal/python_thoughtful_2023/dir_pour_experimentation")
print(list(os.walk(os.getcwd()))) #gives direct tuple
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        print(os.path.join(root,file))

#fibb recursion
def fibb(n):
    if n<=0:
        return "please enter positive n"
    elif n==1 or n==2:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)

#lcm_array
def lcm_array(a=[2,3,4]):
    greater = max(a)    
    for i in range(greater, greater*1000):
        for item in a:
            if i%item !=0:
                break
        if item == a[-1] and i%item==0:
            return i


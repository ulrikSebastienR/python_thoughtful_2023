#inner functions are useful when
def list_patterns(l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1]
):
        '''separates user list to its sublists assuming one sublist will have one pattern only
    comme [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]'''
#matching patterns of list only at first, three ways
#way 1: multiple if else statements with functions only when necessary
#way 2: all functions with trying to group as many of them possible by if else statements inside a single function
#way 3: nested functions are used in this program
#backup functions
        #group multiple functions in one
        def roots(x):
                for number in range(1,int(x/2+1)):
                        if x == number*number:
                                return "square"
                        elif x == number*number*number:
                                return "cube"                        
        def variation(x,y):
                if y == x+1:
                        return "plus 1"
                elif y == x-1:
                        return "subtracted 1"
        #matching pattern using i-1,i, output length equal to input, this is right method
        k = []
        for i in range(len(l)+1):
                try:                        
                        if variation(l[i-1],l[i]):
                                k.append(variation(l[i-1],l[i]))
                        elif roots(l[i]):
                                k.append(roots(l[i]))
                        else:
                                k.append("no pattern in my database")
                except:
                        pass #split k when k[i] = "no pattern in my database"
        split_indices = []
        for i in range(len(k)+1):
                try:
                        if k[i] == "no pattern in my database":
                                split_indices.append(i)
                except:
                        pass
        sublists = [[l[0:split_indices[0]-1],l[split_indices[0]:split_indices[1]-1],l[split_indices[1]:len(l)-1]]]
        return sublists, split_indices

#another example
def iffun2(x): #nested function and true false in if fun:
        def funx(x):
            if x:
                return True
            return False
        if funx(x):
            return x**2
        return x**200  
l = []
for x in range(10):
    l.append(iffun2(x)) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 

#NEW FEB 13, 2024
#& AND | FOR SETS
#COMPARE TWO LISTS/TUPLES

l1, l2, l3 = [num for num in range(5)], [item for item in range(1,6)], [i for i in range(5)]
#l1 and l3 are equal but not l2
print(l1==l2) #False #method 1 : equality o
print(l1==l3) #True
from collections import Counter
print(Counter(l1)==Counter(l2)) #False #METHOD 2 : COMPARE COUNTERS
print(Counter(l1)==Counter(l3)) #True
res = [item for item in l1+l3 if item not in l1 or item not in l3] #USING LIST COMPREHENSION
res1 = [item for item in l1+l2 if item not in l1 or item not in l2] #lists are equal if res = [] or unequal if res != []

#SET INTERSECTION AND SET UNION
print(set(l1) & set(l2))
print(set(l1) | set(l2))

#REVISION FEB 13, 2024
#EXPONENT WITHOUT USING INBUILT FUNCTION





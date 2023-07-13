#use switch from python 3.10+ for multiple if else statements
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1]
#multiple problems exist

def substrings(s):
        "separate words in the string and non words"
        return s1, s2

def longest_substring_without_repeating_characters(s):
    return s1

def strings_patterns(s):
    "breaks string into its component concotaneted substrings of different patterns"
    return s1


def list_patterns(l):
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
                     
        

#matching pattern using i,i+1 #output length 1 less than input
j = []
for i in range(len(l)+1):
         try:
                if roots(l[i]):
                        j.append(roots(l[i]))
                elif variation(l[i],l[i+1]):
                        j.append(variation(l[i],l[i+1]))
                else:
                        j.append("pattern not in my db")
         except:
                pass

#backup functions


def increment(x,y):
    if y == x+1:
        return "plus 1"

def subtract1(x,y):
    if y == x-1:
        return "subtact one"

def match(x,y):
    "trying nesting"
    def square(x):
        for number in range(int(x/2+1)):
            if x == number*number:
                break
        return number
    return square(x)

def sqroot(x):
            for number in range(int(x/2+1)): 
                if x == number*number:
                    return number # return here will output none when sq root is float
                    break
            #return number will always output last value of iterator number when sq root is float, 
                
def cuberoot_while(x):
    number = 1
    while number<int(x/2+1):
        if x != number*number*number:
            number +=1
        else:
            return number      
                      

def list_patterns1(l):#this program is incomplete
        "or do with if else statements and functions when required"
        pattern = []
        for i in range(len(l)+1):
                try:
                    if l[i] == l[i-1]+1: #note you can either match by writing logic
                            pattern.append("increment 1")
                    elif square(l[i]): #or by passing through function
                        pattern.append("square")
                    elif subtract1(l[i],l[i-1]):
                        pattern.append("subtract 1")
                    elif cuberoot_while(l[i]):
                            pattern.append("cube")
                    else:
                        pattern.append("pattern unknown")
                except:
                        pass
        return pattern



    


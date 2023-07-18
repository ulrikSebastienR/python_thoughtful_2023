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

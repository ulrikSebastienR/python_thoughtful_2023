def root(n):
    "calculates square root of a given number"
    for number in range(1,int(n/2+1)):
        if n == number*number:
            return f"{n} is square of {number}"
            break
        #break other way to break loop if you dont want any exit condition
        '''else:
            pass
            #return "not square of any integer" if you want to be definitive
            #otherwise function returns none at its own as explained below'''
        
l, a = [4,9,10], [] #checking multiple numbers for a function
for item in l:
    a.append(root(item)) # ['4 is square of 2', '9 is square of 3', None]

##if root(16): #testing multiple functions
##    a.append("tested for 16") 
##    
##if root(25):
##    #you can get any output here as if condition is true

if root(35):
    print("d") # d is not printed as root(35) tests false

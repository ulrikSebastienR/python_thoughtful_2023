#PROBLEMS ON VARIOUS PROGRAMMING SITES THAT DO NOT FALL TO ANY PROPER CATEGORY

class LeetCodeProblems:
    def __init__(self):
        pass    
    def phone_number_from_alphabets(self, us_style = "1gal9" ):
        "make phone number from US style phone numbers"
        in_numbers = [] 
        #in_numbers = method1() local variable method1 referenced before assignment
        def method1():
            "using ord and lists"
            in_numbers = []
            for item in us_style:
                #print(type(item)) #all items are strings
                #print(ord(item)-ord('0'))
                if 0<=(ord(item)- ord('0'))<=9:
                    in_numbers.append(item)
                elif item in ['a','b','c']:
                    in_numbers.append(2)
                elif item in ['g','h','i']:
                    in_numbers.append(4)
                elif item in ['j','k','l']:
                    in_numbers.append(5)        
            return in_numbers
        def method2(): #PENDING let user choose one of the methods
            in_numbers = []
            lookup = dict(a=2,b=2,c=2,A=2,B=2,C=2,D=3,d=3,e=3,E=3,F=3,f=3,g=3,h=3,i=3,j=4,k=4,l=4)
            #cant do 2=2 for setting key, value pair in a dictionary
            for item in us_style:
##                if type(item)==int:#cant match type because all items are type int
##                    in_numbers.append(item)
                if 0<=ord(item)-ord('0')<=9:
                    in_numbers.append(int(item))
                    #print(in_numbers)
                else:
                    for k,v in lookup.items():
                        if item == k:
                            in_numbers.append(v)                                             
            return in_numbers
        def method3():
            return in_numbers
        #in_numbers = method3()
        #return method2() #return inner function to check working
        return int("".join(str(_) for _ in method2()))    

    def incomp_combination_of_phone_numbers(self,us_style="2isa143",simple=3542):
        "check possible alphabets combinations of a phone number given"
        lookup = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l']}
        combs,temp = [],[]
        for char in us_style:
##            if type(char)==int: all characters in a string are all of type str
            if 0<=ord(char)-ord('0')<=9:
                combs.append(int(char))
            else:
                combs.append(char)
        for item in combs:
            for k,v in lookup.items():
                if item==k:                    
                    temp.append(v)
                else:
                    pass
        return temp
                
lcp = LeetCodeProblems()

class LeetCodeSolutions:
    "others solutions to the leetcode problems not mine"
    def __init__(self):
        self.nums = [num for num in range(20)]
    
    def two_sum(self):
        pass
        
lcs = LeetCodeSolutions()


        
    
#use of ord to convert integers 
##for number in [number for number in range(12)]:
##    print(ord(str(number))-ord('0')) #ord cant find integers greater than 9

def anagram(s):
    l = [char for char in s]

def palindrome_strings(s1,s2):
    "checks if s1 is reversed of s2"
    length = len(s1)
    s = []
    if len(s2) == length:
        for i in range(len(s1)):
            s[length-i-1] = s1[i]
        if s == s2:
            return length
    else:
        return "not palindrome"    
#check = palindrome_strings("madam", "madam")


        
sqrt  = []
def root(n):
    temp, dif = 0, n
    for i in range(1,int(n/2)+1):
        diff = n-i*i
        if diff < dif and diff>0:
            dif = diff
            temp = i
        #continue
    sqrt.append(temp)
    return sqrt

x = root(40)

lookup = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l']}
simple = 5243
sublists = list(lookup.values())
possible = []
for i in range(len(list(lookup.values()))):
    l = []
    for j in range(3):
        l.append(sublists[i])
        

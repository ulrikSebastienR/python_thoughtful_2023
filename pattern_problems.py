#use switch from python 3.10+ for multiple if else statements
list_to_check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1]
string_to_check = ""
#multiple problems exist

class PossiblePatterns:
        "Possible Patterns for both lists and strings"
        def __init__(self):
                pass
        def increment(self, item1, item2):
                 if item2 == item1+1:
                                return "incremented 1"
        def decrement(self,item1,item2):
                if item2 == item1-1:
                        return "decremented 1"
        def sqroot_for(self, number):
                for i in range(number/2):
                        if number == i*i:
                                return i
                                break
        def cuberoot_while(self,number):
                i=1
                while i!=number/3:
                        if number == i*i*i:
                                return i
                                break
                        else:
                                i+=1
        def indices_split(self,l):
                split = []
                for i in range(1,len(l)):
                        if l[i] != l[i-1]:
                                split.append(i)
                return split
        def substring_with_longest_sum(self,l):
                pass
                               
pp = PossiblePatterns()

class MatchingPatterns:
        def __init__(self, entered, item1=None, item2=None, pattern=[]):
                "class to match patterns using functions described in class Possible Patterns"
                self.entered = entered                
                self.item1 = item1
                self.item2 = item2
                self.pattern = pattern
                #pattern = [] this doesn't work
        def list_matching(self):
                for i in range(len(self.entered)):
                        if pp.increment(self.entered[i-1],self.entered[i]):
                                self.pattern.append(pp.increment(self.entered[i-1],self.entered[i]))
                        else:
                                self.pattern.append("pattern not found")
                return self.pattern
        def string_matching(self):
                pass        
mp = MatchingPatterns(list_to_check,1, 2)                                                                                    
      

class StringsPatterns:
        "breaks string into its component concotaneted substrings of different patterns"
        def __init__(self,s="heart",s1="earth"):
                self.s1 = s1
                self.s = s
        def anagram(self):
                "check if two strings are anagram"
                if set(self.s1) == set(self.s):
                        return f"{self.s1} and {self.s} are anagram strings"
                else:
                        return f"{self.s} and {self.s1} are not anagram"                
        def substrings(self):
                "separate words and non words in the given string"
                pass
                return s1, s2
        def palindrome(self):
                "check if a string is palindrome"
                pass
        def all_palindrome_substrings(self):
                "all palindrome substrings in a string"
                pass
x = StringsPatterns()
y = StringsPatterns("madamoiselle","madam")

class NumberPatterns:
        def __init__(self, n = 1231231231234567890):
                self.n = n
        def repeating_numbers(self):
                "find how many times 123 is repeated in 1231231231234567890"
                s = str(self.n)                
                sublists = []
                for i in range(len(s)):
                        for j in range(len(s)):
                                if j>i:
                                        sublists.append(s[i:j])
                repeated, d = {}, {}
                for item in sublists:
                        i = 0
                        for item1 in sublists:
                                if item == item1:
                                        i+=1
                        if i>1:
                                repeated.update({item:i})               
                for k,v in repeated.items():
                        if v == list(reversed(sorted(repeated.values())))[0]:
                                d.update({k:v})                             
                return d, repeated
        def number_to_list(self):
                pass
np = NumberPatterns()                              
                   
class ListPatterns:
        "various list patterns"
        def __init__(self, l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 6,5,4,3,2,1]):
                self.l = l
        def find_range(self):
                "find the biggest range included in your list"
                pattern = []
                for i in self.l:
                        if self.nested_patterns_functions().increment(self.l[i],self.l[i+1]):
                                pattern.append(self.nested_patterns_functions().increment(self.l[i],self.l[i+1]))                               
                return pattern
        def indices_of_a_pattern(self):
                "find starting and ending indices for the pattern you have identified"
                pass
        def split_indices(self):
                "split indices for all the patterns"
                pass
        def missing_positive_at_the_end(self):
                "assume missing positive at the end of the pattern first missing positive from the pattern you identified"
                pass
        def first_missing_positive(self):
                "your pattern can contain multiple missing positive, you need to identify only the first"
                pass
        def all_missing_positives(self):
                "find all missing positives in the pattern you identified"
                pass
##        def nested_patterns_functions(self):
##                "all functions to check for patterns, trying to nest them into one"
##                def increment(self,item1,item2):
##                        if item2 == item1+1:
##                                return "incremented 1"
##                def decrement(self,item1,item2):
##                        if item2 == item1-1:
##                                return "decremented 1"
                
lp = ListPatterns()

class PatternProblems:
        def __init__(self,l=[],s=""):
                self.l = l
                self.s = s
        def merge_intervals(self):
                "merge overlapping intervals leetcode"
                pass
pp = PatternProblems()

class ParenthesisProblems:
        def __init__(self, paren_string=")()())()()()()())()()((("):
                self.paren_string = paren_string
        def match_paren_single(self,paren_right = "()()()"):
                "proof of concept for single sublist of closing parentheses"
                to_match = []
                for i in range(0,len(paren_right),2):
                        print(paren_right[i],ord(paren_right[i]),paren_right[i+1],ord(paren_right[i+1]))
                        if (ord(paren_right[i]),ord(paren_right[i+1])) == (40,41):#use of tuples for matching more than one items
                                to_match.append(True)#match with paren_right[i]=="(" will fail
                        else:
                                to_match.append(False)
                if all(to_match):
                        return paren_right, len(paren_right)
        def all_sublists(self):
                "all pair of parentheses possible/all sublists possible"
                sublists = []
                for i in range(len(self.paren_string)):
                        for j in range(len(self.paren_string)):
                                if j>i:
                                        sublists.append(self.paren_string[i:j])
                return sublists                                        
        def sublists_starting_proper_at_opening_parenthesis(self):
                "seperate all sublists that start at ( and has even length like ()()() = 6, only these sublists should be considered "
                all_parenthesis = self.all_sublists()
                starting_proper, d = [], {}                
                for sublist in all_parenthesis:
                        if ord(sublist[0]) == 40 and len(sublist)%2==0:#matching without ord will fail
                               starting_proper.append(sublist)                                                        
                return starting_proper
        def proper_closing_parenthesis(self):
                "all parentheis sublists that close properly"
                do = self.sublists_starting_proper_at_opening_parenthesis()
                d,correct = {},[]
                for sublist in do:
                        status = []
                        for i in range(0,len(sublist),2):
                                if (ord(sublist[i]),ord(sublist[i+1]))==(40,41):
                                        status.append(True)
                                else:
                                        status.append(False)
                        d.update({sublist:status})
                        if all(status):
                                correct.append(sublist)                                
                return correct,d
        def longest_proper_parenthesis(self):
                all_proper = self.proper_closing_parenthesis()[0]
                ours = max(len(item) for item in all_proper)
                answer = [item for item in all_proper if len(item)==ours]#will be generator expression if we do str(item for) or (item for) and syntax error if we take value without parenthesis ie item for
                return answer
        def range_to_slice_only_even_or_odd_indices_items(self):#INCOMPLETE aug 9, 23
                "range function can used to filter only even or odd indices items"
                sublists,true_false_status,ordered = [], {},[]
                for i in range(len(self.paren_string)):                     
                        for j in range(len(self.paren_string)):
                                if j>i:
                                        sublists.append(self.paren_string[i:j])
##                for sublist in sublists:
##                        closing_paren = []
##                        for i in range(0,len(sublist),2): #will work for only even indices if we do range(0,len(sublist),2) and for odd indices if we do range(1,len(sublist),2)
##                                try: #problem here is try except which messes indices and doesn't identify (), so needs to separate all substrings that strat with (
##                                        if (ord(sublist[i]),ord(sublist[i+1])) == (40,41):
##                                                closing_paren.append(True)
##                                        else:
##                                                closing_paren.append(False)
##                                except:
##                                        pass
##                        true_false_status.update({sublist:closing_paren})
##                for sublist in sublists:
##                        closing_paren = []
##                        for i in range(1,len(sublist),2): #will work for only even indices if we do range(0,len(sublist),2) and for odd indices if we do range(1,len(sublist),2)
##                                try:
##                                        if (ord(sublist[i]),ord(sublist[i+1])) == (40,41):
##                                                closing_paren.append(True)
##                                        else:
##                                                closing_paren.append(False)
##                                except:
##                                        pass
##                        true_false_status.update({sublist:closing_paren})
                for sublist in sublists:
                        closing_paren = []                        
                        for i in range(len(sublist)): #will work for only even indices if we do range(0,len(sublist),2) and for odd indices if we do range(1,len(sublist),2)
                                try:
                                        if (ord(sublist[i]),ord(sublist[i+1])) == (40,41):
                                                closing_paren.append(True)
                                        else:
                                                closing_paren.append(False)
                                except:
                                        pass
                        true_false_status.update({sublist:closing_paren})
                        
                        
##                        if all(closing_paren):
##                                ordered.append(sublist)
                return true_false_status#, ordered, sublists       
prp = ParenthesisProblems()


                


                



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

#NOTES
l,pattern,pattern1 = [number for number in range(8)],[],[]
for i in range(len(l)):
    if l[i] == l[i-1]+1: # it is the right method 
        pattern.append("increment") #['increment', 'increment', 'increment', 'increment', 'increment', 'increment', 'increment']
    if l[i+1] == l[i]+1:
        pattern1.append("increment") #list index goes out of range ['increment', 'increment', 'increment', 'increment', 'increment', 'increment', 'increment']

    


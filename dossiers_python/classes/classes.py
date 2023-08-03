#class can access outside variables and functions just by referring with their names
s = "dar gai" #these are needed for later mindfulness class
def length(string="dalian russia and japan ruled too"): #needed for later mindfulness class
    i = 0
    for char in string:
        i += 1
    return i
        
class MindfulNess:
    "class can access outside variables and functions by just referring with their names"
    def __init__(self, l=[char for char in "sample list"]):
        self.l = l
    def method1(self):
        return s #a class can access outside variable without global
    def length_of(self):
        return length(self.l) #class can access outside functions too without using global 
mfn = MindfulNess()

class LearningClass:
    def __init__(self,l=[],s=""):
        self.s = s
        self.l = l #in class definition order does not matter
    def fun_inside_variable(self): #giving self is mandatory rest function can use its own inside variable as are used in normal functions 
        a,b,*c = [number for number in range(5)] #one liner assignment 
        return a,b,c #(0, 1, [2, 3, 4])
    def passed_from_outside(self,n): #function can accept arguments/parameters from outside in addition to instance variables just like a normal function
        pfc = self.fun_inside_variable()[-1] #self is to be used to call another function inside class
        pfc.append(n) 
        return pfc #[2, 3, 4, 1000]
lc = LearningClass([0])

#access another class method
class ListOperations:
    def __init__(self,l1=[_ for _ in range(10)],l2=[_ for _ in range(5)]):
        self.l1 = l1
        self.l2 = l2
    def subtract_l2_from_l1(self):
        diff = [item for item in self.l1 if item not in self.l2]
        return diff
lo = ListOperations()

class StringOperations:
    "make it a class that has common operations on strings other classes will refernce methods from this class"
    def __init__(self,s="hope is a fancy word"):
        self.s = s
    def subtract_strings(self,s1):
        diff = "".join([_ for _ in list(self.s) if _ not in list(s1)]) #s1 is to be input by the user or come from outside the class
        return diff
    def subtract(self, s1): #access another class method 
        diff = ListOperations(list(self.s),list(s1)).subtract_l2_from_l1()
        return "".join(diff)
so = StringOperations()

#keyworded arguments as instance variables and if possible class variables

# if else in class definition, wanted this class methods to be executed only if student is in middle standard

class Progress1:
    def __init__(self,  standard):
        self.standard = standard
    def gpa(self):
         if self.standard != "middle":
            return "you did not appear for middle grade"
         else:
            return "hola"
b = Progress1("neuf") #now b.gpa() will give the intended answer

class Progress:
    def __init__(self, standard):
        self.standard = "middle" #will set standard for chaque instance
        #self.standard = standard == "middle" will also set standard pour chaque instance
    def gpa(self):
        if self.standard != "middle":
            return "you did not appear for middle grade"
        else:
            return "hola"
a = Progress("neuf") #now print a.gpa() answer is hola as standard for each instance was already set in class definition





 
        
#savings account, creation of fd and updatation of balance in savings account

#make deposit account to check first if the savings account has the correct balance
        

# a class variable vs instance variable example
class Result:
    school = "Ecole de Polytechic, epfl"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def gpa(self):
        return f"{self.name} passed with A" if self.marks>90 else "be prepared next time"
       

r = Result("matew", 86) #verify by printing Result.school and r.school

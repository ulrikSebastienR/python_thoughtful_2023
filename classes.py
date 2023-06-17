#all on classes

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

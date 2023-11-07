##CLASSES BASICS

outside_var = 10
class UnderstandingClassandInstanceVariables:
    class_var = 1
    "Understanding how the class variables are called within the class"
    def __init__(self, instance_no=3, power=5):
        self.instance_no = instance_no
        self.power = power
    def outside_var_method(self):
        return outside_var**self.power #a class can access global variable by reference only
    def class_var_method(self):
        "using self to address the class variable"
        #return class_var**self.power    #error - class_var is not defined
        return self.class_var*10 #can access class variable by using self
    def class_var_method2(self):
        "using instance name"
        return uv.class_var*10 #10, can access using instance or class name
    def class_var_method3(self):
        return UnderstandingVariables.class_var*10 #10, can access using instance or class name
    def class_var_method4(self):
        return type(self).class_var*10 #10, can access using type(self)

uv = UnderstandingClassandInstanceVariables()



##FUNCTION BASICS
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


outside_var = 10
class UnderstandingVariables:
    class_var = 1
    "Understanding how the variables are called from class"
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
        

uv = UnderstandingVariables()


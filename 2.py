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
        #return class_var**self.power    #error - class_var is not defined
        return None
uv = UnderstandingVariables()


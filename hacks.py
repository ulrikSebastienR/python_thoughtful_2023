import ds_operations

class UsefulHacks:
    def __init__(self, l=ds_operations.dso.ds1,s=ds_operations.dso.s): #passing values from another file
        self.l = l
        self.s = s
    def Range_to_generate_floats(self):
        temperatures = [temp/10 for temp in range(20,480,5)]
        return temperatures
    
        
uh = UsefulHacks()

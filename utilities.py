#taking dob or various numbers, good one, needs to be thoroughly checked
##print("enter your dob in yyyy mm dd format")
##ui = list(map(int, input().split()))
##
##import datetime
##dob = datetime.date(ui[0],ui[1],ui[2])#this line makes sure that dates and months are in the correct range as they should be

class RandomModule:
    #import random
    "using random module for various utilites"
    def __init__(self, l=[]):
        self.l = l
        #import random

    def list_random_integers(self):
        "generate a list containing only random integers useful for lcm hcf etc"
        import random #random should be imported inside the function wont work in class definition
        lrints = [random.randint(10,50) for i in range(10)]
        return lrints

rm = RandomModule()

#ordereddicts are not needed now as from python 3.6 onwards dictionaries remember the order
#mutation doesnt change id while reassignment does
        
        


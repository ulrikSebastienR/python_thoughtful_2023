class TrueFalse:
    def __init__(self):
        pass
    def true_false(self): #0,empty lists, tuples are false
        "shows control flow in for loop as well"
        for i in range(10):
            if i: #note at i = 0, its false for python, rest is true
                print("Natalia", i)
            print("Distraction", i)
    def value(self,i): #experiment avec i=0 and i=1
        if i: 
            return i
        else:
            return "False"
    def iffun2(self,x): #nested function and true false in if fun:
        def funx(x):
            if x:
                return True
            return False
        if funx(x):
            return x**2
        return x**200
    
tf = TrueFalse()
l = []
for x in range(10):
    l.append(tf.iffun2(x)) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 

class UnderstandingReturn:
    def __init__(self):
        pass
    def understanding_return(self):
        for i in range(10): #range starts at 0
            if i:
                return i
            return "out" #"out" because i = 0 is false 
        return "big"
    def understanding_return1(self):
        for i in range(1,10): #range starts at 1
            if i:
                return i #output is 1, break is already implemented
            return "out"
        return "function out"
ur = UnderstandingReturn()            




    

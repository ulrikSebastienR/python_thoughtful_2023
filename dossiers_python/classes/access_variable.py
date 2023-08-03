#access one class variables from another class
##https://stackoverflow.com/questions/19993795/how-would-i-access-variables-from-one-class-to-another
#accessing class variables is easy
class A:
    a = 1
    def __init__(self,a1):
        self.a1 = a1

class B:
    b = 2
    def __init__(self, b2, b20):
        self.b2 = A.a
        #self.b20 = how to write a's instance in 

x = A(10)
y = B(20)
#need to see to return instance variables


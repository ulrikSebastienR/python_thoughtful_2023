# try except
import datetime
y = input("enter your year of birth")

try:
    dob = datetime.date(y, m, d)
except:
    print("please enter only valid real numbers")

#try except 2
class Make7:
   # n = 7 class variable
    "find all numbers that when added make 7" 
    def __init__(self,n=7,l=[[char] for char in "abcde"]): #no need to pass any instance variables if you have initialized them in class definition, these are positional arguments with default values
        self.n = n
        self.l = l
        self.r = [number for number in range(int(self.n/2+1))]
   
    def removal_from_r_wrong1(self): #should never be attempted deletion of elements from list under current iteration
        "removing numbers from r after loop runs"
        print(self.r)
        for number in self.r:
            print(f"number is {number}")
            for sublist in self.l:
                try:
                    sublist.append(number)
                    sublist.append(self.n-number)
                    print(f"l is {self.l}")
                    print(f"number after sublist loop is {number}")
                    #self.r.remove(number) [[0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5]]
                    #print(f"r is {self.r}")
                except:
                    pass
            print(f"number after sublist loop is {number}") #CANT UNDERSTAND WHY LOOP NEVER GOES TO 1 AND 3
            self.r.remove(number) #[[0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5], [0, 7, 2, 5]]
        for sublist in self.l:
            sublist.pop(0)
        return self.l
x = Make7()
    

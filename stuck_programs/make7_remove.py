#import pdb
#pdb.set_trace()
class Make7:
   # n = 7 class variable
    "find all numbers that when added make 7" 
    def __init__(self,n=7,l=[[char] for char in "abcde"]): #no need to pass any instance variables if you have initialized them in class definition, these are positional arguments with default values
        self.n = n
        self.l = l
        self.r = [number for number in range(int(self.n/2+1))]

    def failed2(self):
        print(self.r)
        for sublist in self.l:
            print(f"1{sublist}, {self.r} at start of sublist loop")
            #breakpoint()
            for number in self.r:
                print(f"2{self.r} and number is {number} at start of number loop")
                sublist.append(number)
                sublist.append(self.n-number)
                print(f"3{sublist}, {self.r} and number is {number} at the end of number loop")
                self.r.remove(number)
                print(f"4{self.r} and number is {number} after removing {number}")
            sublist.pop(0)
        #print(self.l, self.r)
        return f"returned values are {self.l}, {self.r}"
    

x = Make7()

##[0, 1, 2, 3]
##1['a'], [0, 1, 2, 3] at start of sublist loop
##2[0, 1, 2, 3] and number is 0 at start of number loop
##3['a', 0, 7], [0, 1, 2, 3] and number is 0 at the end of number loop
##4[1, 2, 3] and number is 0 after removing 0
##2[1, 2, 3] and number is 2 at start of number loop
##3['a', 0, 7, 2, 5], [1, 2, 3] and number is 2 at the end of number loop
##4[1, 3] and number is 2 after removing 2
##1['b'], [1, 3] at start of sublist loop
##2[1, 3] and number is 1 at start of number loop
##3['b', 1, 6], [1, 3] and number is 1 at the end of number loop
##4[3] and number is 1 after removing 1
##1['c'], [3] at start of sublist loop
##2[3] and number is 3 at start of number loop
##3['c', 3, 4], [3] and number is 3 at the end of number loop
##4[] and number is 3 after removing 3
##1['d'], [] at start of sublist loop
##1['e'], [] at start of sublist loop
##'returned values are [[0, 7, 2, 5], [1, 6], [3, 4], [], []], []'



        
   

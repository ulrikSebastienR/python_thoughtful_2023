#daily practice programs,
#sep 27 trying out reversed and sorted and reverse and sort a list and string
l, s = [12,2,21,25,93,11,7,81,18,30], "the secret life of walter mitty\n marley and me\n la cour"
d = dict(a=1,b=2)
l1 = l #for id and copy 
l2 = l.copy()

#import pandas as pd

def hcfthreenos(a=13,b=15,c=41): #INCOMPLETE
        smaller = min(a,b,c)
        for i in range(2,smaller+1):
            if a%i==0 and b%i==0 and c%i==0:
                return i
        else:
            return "no factor exists for these numbers" #tested for 13,15,41 

def anagram(s):
    l = [char for char in s]




        
sqrt  = []
def root(n):
    temp, dif = 0, n
    for i in range(1,int(n/2)+1):
        diff = n-i*i
        if diff < dif and diff>0:
            dif = diff
            temp = i
        #continue
    sqrt.append(temp)
    return sqrt

x = root(40)
    

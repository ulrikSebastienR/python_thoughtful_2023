def anagram(s):
    l = [char for char in s]

def palindrome_strings(s1,s2):
    "checks if s1 is reversed of s2"
    length = len(s1)
    s = []
    if len(s2) == length:
        for i in range(len(s1)):
            s[length-i-1] = s1[i]
        if s == s2:
            return length
    else:
        return "not palindrome"    
#check = palindrome_strings("madam", "madam")


        
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
    

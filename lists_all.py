#in all list methods, you can not do l= l.remove(i) as l will be none type now
# Program examples are at the end of this file
#convert list to dictionary
def list_to_dict(l):
    d = dict(enumerate(l))
    return d
#making a nested list
list_nested = [[1]]*6

#extend in lists
a = [[1,-2,3,-4],[-10,21,-32,40]]
a1, a2 = [i for i in a]
a1.extend(i for i in a2)
#making new reversed list by extend or you can do l.reverse
l_string = [char for char in "madamoiselle"]
lreversed = []
lreversed.extend(l_string[len(l_string)-1-i] for i in range(len(l_string)))


#l1 = l2
numbers = [i for i in range(20)]
even = [i for i in range(20) if i%2 == 0]

#subtract
odd = [i for i in numbers if i not in even]
#see if a list is subset of another list
x = all(even) in numbers #outputs True if x is subset of numbers

# merge to make exactly identical to original list
new_numbers = []
for i, j in zip(even, odd):
    new_numbers.append(i)
    new_numbers.append(j)

#do numbers + even but exclude the repeating
merged_repeated = numbers + even

for i in merged_repeated:
    if merged_repeated.count(i) > 1:
       merged_repeated.remove(i)

l1 = [char for char in "abcdefghijklmn"]
l2 = [char for char in "0123456789"]
#INTENDED OUTPUT = "aBcDe" DONE



l = []
i = len(l1) if len(l1) < len(l2) else len(l2)
for j in range(i):
    l.append(l1[j] if j%2 == 0 else l2[j])

#INTENDED OUTPUT = a0b1c2--i9jklmn DONE

l_extended = []
i_big = len(l1) if len(l1)>len(l2) else len(l2)

for j in range(i_big):
    if j < i:
        l_extended.append(l1[j])
        l_extended.append(l2[j])
    else:
        l_extended.append(l1[j])
    

#INTENDED OUTPUT = a9b8 DONE
l_mixed = []        
for j in range(i):
    l_mixed.append(l1[j] if j%2==0 else l2[i-j])

#INTENDED OUTPUT = a9b8j0klmn DONE
l_rev = []
for j in range(i_big):
    if j < i:
            l_rev.append(l1[j])
            l_rev.append(l2[i-1-j])
    else:
            l_rev.append(l1[j])
	


#INTENDED OUTPUT = a9b8--i0nmlkj
l_1rev = []

for j in range(i_big):
    if j < i:
        l_1rev.append(l1[j])
        l_1rev.append(l2[i-1-j])  
for k in range(i_big-i):
    l_1rev.append(l1[i_big-1-k])
   
#look at difference in output of these two programs
def program1(n):
    for i in range(5):
        l = [char for char in "abcde"]
        l.remove(l[i])
        #print(l[i])
    return l

def program2(n):
    for i in range(5):
        l = [char for char in "abcde"]
        print(l[i])
        l.remove(l[i])
    return l

for j in range(len(l)-1, 0,  -1):
    print(l[j])
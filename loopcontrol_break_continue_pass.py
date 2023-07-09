#continue takes control back to first line of the loop, break terminates any loop and pass does nothing
#you can update item to traverse (like a list) in the loop itself and loop will traverse the updated list from next iteration
#while loop can not update itself and you need to provide value of iterator for the next step otherwise it will keep on hanging on the very first iteration
l = [number for number in range(6,66,6)]
print(l)

#simplest
for i,item in enumerate(l):
    if item%4==0:
        print(item)
print("----")

#using while 
for i in l:
    #print("-")
    while i %4==0:
        print(i)
        i += 6
print("------")    

# a better way to do above
for i in range(len(l)):
    #print(i,l[i])
    while l[i]%4 ==0:
        print(l[i])
        i += 1
        if i == len(l):
            break
print("-----")

#continue throws control back to start of the loop ignoring all remaining statements
for i,item in enumerate(l):
    if item%4==0:
        print(item)
        continue
        print(i,item)
print("----- DOING VIA ENUMERATE AND WHILE")

#doing via enumerate and while
for i,item in enumerate(l):
    while item%4 ==0:
        print(item)
        i+=1
        break

print("SOME EXAMPLES ON WHILE")

print("SORT A LIST USING WHILE")
l1 = [31, 23, 83, 12, 86, 97, 34, 18]
l_s = []
while len(l1)!=0:
    l_s.append(min(l1))
    l1.remove(min(l1))
print(l_s)

#if a number is prime using while loop
n = 13
i = 2
while i!=n-1:
    if n%i ==0:
        break
    i +=1
    if i == n-1:
        print(f"{n} is a prime number")

#if a number is prime using for loop
for i in range(2,n):
    if n%i ==0:
        break
    else:
        pass
    if i == n-1:
        print(f"{n} is a prime number by for loop")        

def example1():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for number in [1,2]:
        for sublist in l:
            sublist.append(number)
            print(l)
    return l #output [['a', 1, 2], ['b', 1, 2]]

def example2():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for number in [1,2]:
        for sublist in l:
            sublist.append(number)
            print(l)
            break
    return l #output [['a', 1,2], ['b']]

def example3():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for number in [1,2]:
        for sublist in l:
            sublist.append(number)
            print(l)
            break
        break
    return l #output [['a',1], ['b']]

def example4():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for number in [1,2]:
        for sublist in l:
            sublist.append(number)
            print(l)
            break
    #break
    return l #output break outside loop error

def illustration1():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    l = [[char] for char in "ab"]
    for sublist in l:
        for number in [1,2]:
            sublist.append(number)
            print(l)
    return l #output [['a', 1, 2], ['b', 1, 2]]

def make5_1():
    "example on break, break truncates the current loop and continue passes the control back to begining of the loop "
    n = 5
    l = [[char] for char in "abcde"]
    r = [number for number in range(1,int(n/2+1))]
    try:
        for number in r:
            print(r)
            for sublist in l:
                print(r)
                print(number)
                sublist.append(number)
                sublist.append(n-number)
                print(l)
                r.remove(number)
                print(f"r is {r}")
                print(l)
        #return l #[['a', 1, 4], ['b', 1, 4], ['c'], ['d'], ['e']]
    except: #to bypass the error x not in list as list finally has no elements
        pass
    return l
    




        


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


        

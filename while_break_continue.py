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
        


        


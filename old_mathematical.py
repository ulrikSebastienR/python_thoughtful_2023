#greatest/shortest of given numbers
class Great:
    ''' Class to calculate greatest of given numbers in a list'''
    def __init__(self, user_list):
        self.user_list = user_list

    def greatest(self):
        ''' function calculates greatest of numbers given in a list'''
        greatest = self.user_list[0]
        for item in self.user_list:
            if item > greatest:
                greatest = item
        return greatest 
g = Great([3,45, 95, 100, 204, 32, 12, 21])



#reverse an integer
n,l = 2345, []
quotient = n
while quotient!=0:
    r = quotient%10
    l.append(r)
    quotient = quotient//10
    continue
reverse_n = l[0]*1000+l[1]*100+l[2]*10+l[3] #or
reverse = int("".join(str(i) for i in l))

#prime factorization
#need to test in detail, #this is right but why it never worked le semain predecent
upper, l10 = 2399, [2]
for number in range(2,upper+1):
    for i in range(2,number):
        if number%i ==0:
            break
        else:
            if number%i !=0 and i==number-1:
                l10.append(number)
        
#find all prime numbers in a range using flag, doesnt include 2 
n, prime_numbers = 2399, [2]
for number in range(2, n+1):
    flag = False
    for i in range(2,number):
        if number%i == 0:
            break
        else:
            flag = True
        if i == number-1: #this is done to ensure loop runs to the end otherwise loop will output prime number first time remainder isnt zero
            prime_numbers.append(number)

#prime factorization without recursion
pf = [] #we are referring as quotient the number whose prime factors we are supposed to find like 6 or 15 or 120 etc
def factors(quotient):
    while quotient !=1:
        for number in prime_numbers:
            if quotient%number ==0:
                break
        pf.append(number)
        quotient = quotient//number
    return pf
x = factors(6) #print(pf)

#prime factorization with recursion
pfr =  []
def factorsr(n):
    if n == 1:
        return pfr
    else:
        for number in prime_numbers:
            if n%number==0:
                pfr.append(number)
                n = n//number
        return factorsr(n)
y = factorsr(60)
    
        

#using flag, prime number, better method includes 2 as well
n, flag = 2, False
for i in range(2, n):
    if n%i == 0:
        break
    else:
        flag = True       
    if i == n-1:
        print(f"{n} is a prime number by flag")


#prime numbers in a range using for loop, 1 is not considered a prime number
l, n = [2], 23
for number in range(1,n+1):
    for i in range(2, n):
        if number%i == 0:
            break
        else:
            pass
        if i == number-1:
            l.append(number)

#prime numbers in a range using while loop, while loop cant detect 3 as for 3, i==2
l1, n = [2,3], 234
for number in range(1,n+1):
    i =2
    while i<number:
        if number%i == 0:
            break
        else:
            i+= 1
        if i == number-1:
            l1.append(number) #leaving 3 currently

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

#hcf 
a, b = 32, 128
smaller = a if a<b else b
hcf = 0

for number in range(1,smaller+1):
    if a%number == 0 and b%number ==0 :
        hcf = number
#or one liner
hcf1 = max([number for number in range(1,smaller+1) if a%number==0 and b%number==0])

#lcm
a, b = 3,5
larger = a if a>b else b
lcm = 0

for number in range(larger, larger*1000000):
    if number%a == 0 and number%b == 0:
        lcm = number
        break
#or one liner
lcm1 = min([number for number in range(larger,10000000) if number%a==0 and number%b])



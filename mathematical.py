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

#lcm
a, b = 3,5
larger = a if a>b else b
lcm = 0

for number in range(larger, larger*1000000):
    if number%a == 0 and number%b == 0:
        lcm = number
        break



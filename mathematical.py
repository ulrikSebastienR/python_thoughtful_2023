#prime numbers in a range, incomplete
l,n = [],13

for number in range(1, n+1):
    for i in range(2, number+1):
        if number%i == 0 and i < number:
            continue         
        else:
            l.append(i)


#if a number is prime
n = 14
i = 2
while i!=n-1:
    if n%i ==0:
        break
    i +=1
    if i == n-1:
        print(f"{n} is a prime number")

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



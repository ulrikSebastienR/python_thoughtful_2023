#list comprehension,
l = [n for n in range(20) if n%2==0]
multiple_of_both_2_et_3 = [number for number in range(1000) if number%2==0 and number%3==0]
evenOdd = ["even" if number%2==0 else "odd" for number in range(10)]
#lcm and hcf
a,b = 16,64
smaller = a if a<b else b
larger = a if a>b else b
lcm = min([number for number in range(larger,100000) if number%a==0 and number%b==0])
hcf = max([number for number in range(2,smaller+1) if a%number==0 and b%number==0])


first = [char for char in "abcdefghi"]
second = [number for number in range(10)]
third = [number for number in range(100,200,10)]
#define via one liner list comprehension
dx = {k:v for k, v in zip(first, second)}
dy = dict(zip(third,first))
#merge dictionary in one line
d = {**dx, **dy}

#not working
'''l = []
l = [n for n,i in zip(range(1,13), range(2,n)) if n%i==0]'''

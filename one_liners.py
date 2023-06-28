#list comprehension,
l = [n for n in range(20) if n%2==0]

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

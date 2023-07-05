l = [[]]*6
n = 5
r = [number for number in range(int(n/2)+1)]

for sublist in l:
     for number in r:
         sublist.append(number)
         sublist.append(n-number)
         break
     r.remove(number)
     #break gives output [[0, 5], [0, 5], [0, 5], [0, 5], [0, 5], [0, 5]]
     #continue or without continue gives [[0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3], [0, 5, 1, 4, 2, 3]]
     
     

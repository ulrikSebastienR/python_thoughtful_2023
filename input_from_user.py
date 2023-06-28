#taking dob or various numbers
print("enter your dob in yyyy mm dd format")
ui = list(map(int, input().split()))

import datetime
dob = datetime.date(ui[0],ui[1],ui[2])

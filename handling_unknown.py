# try except
import datetime
y = input("enter your year of birth")

try:
    dob = datetime.date(y, m, d)
except:
    print("please enter only valid real numbers")

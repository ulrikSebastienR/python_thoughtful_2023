from datetime import date, datetime
import inflect
import sys

def sub_date(dob):
try:
b=date.fromisoformat(dob)
except ValueError:
sys.exit("invalid date type")
else:
today = http://date.today()
sub = today - b
time=http://sub.total_seconds()/60
return int(time)

def convert(num):
p=inflect.engine()
return f"{p.number_to_words(num, andword='').capitalize()} minutes"

def main():
dob=input("enter date of birth: " ).strip()
time=sub_date(dob)
print(convert(time))

if __name__=="__main__":
main()

from seasons import sub_date
import pytest
def main():
test_sub_date()

def test_sub_date():
with pytest.raises(SystemExit):
sub_date("09-01-1999")
with pytest.raises(SystemExit):
sub_date("cat")

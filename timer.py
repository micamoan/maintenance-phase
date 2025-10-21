import datetime
import sys

input_date = sys.argv[1]
s = datetime.datetime.strptime(input_date, "%Y-%m-%d").strftime("%a, %d %b %Y 00:00:00 +0000")
print(s)

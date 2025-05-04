#!env python3
#
# Usage
# 	python3 /Volumes/git/github/python/05_datemod/datemod.py 2 && echo "returning true"
#	python3 /Volumes/git/github/python/05_datemod/datemod.py 2 && sh ~/bin/osascript_display_copy "jobs 2"
#	python3 /Volumes/git/github/python/05_datemod/datemod.py 2 && sh ~/bin/osascript_display_copy "jobs 8"

# See also
#
#	/Volumes/git/computers.git/mac/bin/cron_date_modulus.sh
#
import sys
import datetime

# Get the current date
now = datetime.datetime.now()

# Get the day of the year
day_of_year = now.timetuple().tm_yday

if len(sys.argv) < 2:
	print("[warning] to see what day of the year it is, run dayofyear.py", file=sys.stderr)
	print("[error] specify a divisor", file=sys.stderr)
	sys.exit(1)
	
divisor = int(sys.argv[1])

# Calculate the modulus (remainder) when divided by 13
modulus = day_of_year % divisor

# print(f"{divisor} {day_of_year} {modulus}", file=sys.stderr)

# Check if the modulus is zero and print the result
if modulus == 0:
	print(f"[debug] >>\t{divisor} {day_of_year} {modulus}", file=sys.stderr)
	print(0)
	sys.exit(0)
else:
	print(1)
	print(f"[debug] \t{divisor} {day_of_year} {modulus}", file=sys.stderr)
	sys.exit(1)


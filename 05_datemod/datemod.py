#!env python3

import sys
import datetime

# Get the current date
now = datetime.datetime.now()

# Get the day of the year
day_of_year = now.timetuple().tm_yday

if len(sys.argv) < 1:
	print("specify a divisor", file=sys.stderr)
	
divisor = int(sys.argv[1])

# Calculate the modulus (remainder) when divided by 13
modulus = day_of_year % divisor

# print(f"{divisor} {day_of_year} {modulus}", file=sys.stderr)

# Check if the modulus is zero and print the result
if modulus == 0:
	print(f">>\t{divisor} {day_of_year} {modulus}", file=sys.stderr)
	print(0)
	sys.exit(0)
else:
	print(1)
	print(f"\t{divisor} {day_of_year} {modulus}", file=sys.stderr)
	sys.exit(1)


#!/usr/bin/env python3

#----------------------------------------------------------------------------
# DESCRIPTION		
# DATE				2025
# AUTHOR			ss401533@gmail.com                                           
# USAGE
#	DAY_OF_YEAR=`/Volumes/git/github/python/05_datemod/dayofyear.py` && MOD=`bc --expression="$DAY_OF_YEAR % 2"` && (( $MOD == 0 )) && echo "no remainder"
#----------------------------------------------------------------------------
# template found at ~/.vim/python.temp

import sys
import datetime


if len(sys.argv) < 0:
	print("[error] specify an arg", file=sys.stderr)
	
	sys.exit(1)

# Get the current date
now = datetime.datetime.now()

# Get the day of the year
day_of_year = now.timetuple().tm_yday

print(day_of_year)


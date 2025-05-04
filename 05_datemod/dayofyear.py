#!/usr/bin/env python3

#----------------------------------------------------------------------------
# DESCRIPTION		
# DATE				2025
# AUTHOR			ss401533@gmail.com                                           
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


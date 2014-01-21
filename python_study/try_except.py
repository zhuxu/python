#!/usr/bin/python
# Filename: try_except.py

import sys

try:
	s = raw_input('Enter something -->')
except EOFError:
	print '\nWhy did you do an EOF on me?'
except:
	print '\nSome error/exception occurred.'
	# here. we are not exiting the program

print 'Done'

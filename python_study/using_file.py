#!/usr/bin/python
# Filename: using_file.py

poem = '''\
Programming is fun
when the work is done
if you wanna make your work also fun:
use Python!
'''

f = file('poem.txt', 'w')  # open for writing
f.write(poem)   # write text to file
f.close()   # close the file

f = file('poem.txt')
# if no mode is specified, read mode is assumed by default
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,
	# Notice comma to avoid automatic newline added by python

f.close()   # close the file

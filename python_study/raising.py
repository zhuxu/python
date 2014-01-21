#!/usr/bin/python
# Filename: raising.py

class short_input_exception(Exception):
	'''A user-defined exception class.'''
	def __init__(self, lenght, atleast):
		Exception.__init__(self)
		self.length = lenght
		self.atleast = atleast

try:
	s = raw_input('Enter something -->')
	if len(s) < 3:
		raise short_input_exception(len(s), 3)
	# Other work can continue as usual here
except EOFError:
	print '\nWhy did you do an EOF on me?'
except short_input_exception, x:
	print 'short_input_exception: The input was of lenght %d, \
was excepting at least %d' % (x.length, x.atleast),
else:
	print 'No exception was raised.'

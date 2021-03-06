#!/usr/bin/python
# Filename: using_dict.py
# 'ab' is short for 'a'ddress'b'ook

ab = {
		'Swaroop'   : 'swaroopch@byteofpython.info',
		'Larry'     : 'larry@wall.org',
		'Matsumoto' : 'matz@ruby-lang.org',
		'Spammer'   : 'spammer@hotmail.com'
	}

print "Swaroop's address is %s" % ab['Swaroop']

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'


print '\nThere are %d contacts in the address-book\n' % len(ab)
for name, address in ab.items():
	print 'Contact %s at %s' % (name, address)

# Deleting a key/value pair
del ab['Spammer']

print ""
print '\nThere are %d contacts in the address-book\n' % len(ab)
for name, address in ab.items():
	print 'Contact %s at %s' % (name, address)

if 'Guido' in ab: # OR ab.has_key('Gudio')
	print "\nGuido's address is %s" % ab['Guido']

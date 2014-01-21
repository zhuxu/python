#!/usr/bin/python
# Filename: pickling.py

import cPickle as p
# import pickle as p

shop_list_file = 'shoplist.data'
# the name of the file where we will store the object

shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = file(shop_list_file, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close()

del shoplist # remove the shoplist

# Read back from the storage
f = file(shop_list_file)
storedlist = p.load(f)
print storedlist

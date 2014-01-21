#!/usr/bin/python
# Filename: class_init.py

class Person:
	def __init__(self, name):
		self.name = name;
	def say_hi(self):
		print 'Hello, my name is', self.name

p = Person('Swaroop')
p.say_hi()

Person('zhuxu').say_hi()

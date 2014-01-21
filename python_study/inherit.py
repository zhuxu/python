#!/usr/bin/python
# Filename: inherit.py

class school_member:
	''' Rempresents any school member.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print '(Initialized school_member: %s)' % self.name

	def tell(self):
		'''Tell my details.'''
		print 'Name: "%s" Age:"%s"' % (self.name, self.age),

class teacher(school_member):
	'''Represents a teacher.'''
	def __init__(self, name, age, salary):
		school_member.__init__(self, name, age)
		self.salary = salary
		print '(Initialized teacher: %s)' % self.name

	def tell(self):
		school_member.tell(self)
		print 'Salary: "%d"' % self.salary

class student(school_member):
	'''Represents a student.'''
	def __init__(self, name, age, marks):
		school_member.__init__(self, name, age)
		self.marks = marks
		print '(Initialized student: %s)' % self.name

	def tell(self):
		school_member.tell(self)
		print 'Marks: "%d"' % self.marks

t = teacher('Mrs.Shrividya', 40, 3000)
s = student('Swaroop', 22, 75)

print

members = [t, s]
for member in members:
	member.tell()

"""
Lecture 8: Dictionaries in Python
Momentum Learning
Introduction to Python
M. Bedir Tapkan
"""

# Dictionaries and lists share the following characteristics:

#    - Both are mutable.
#    - Both are dynamic. They can grow and shrink as needed.
#    - Both can be nested. A list can contain another list. 
#       A dictionary can contain another dictionary. 
#       A dictionary can also contain a list, and vice versa.

# Dictionaries differ from lists primarily in how elements 
#   are accessed:
#    - List elements are accessed by their position in the list, via indexing.
#    - Dictionary elements are accessed via keys.

# Defining Dictionaries

# name = {
#			<key> : <value> ,
#			<key> : <value>
#			...
#        }

d = {
	'one': 'melody',
	'two': 'nishadh',
	'three': 'karthik',
	'four': 'krithik'
}

print(d['one'])

# typecasting
num = 1
print(type(num))

num = '1'
print(type(num))

num = int('1') # typecasting to int
print(type(num))

# int()
# str()
# bool()

tx = dict([
	('one', 'Houston'),
	('second', 'Dallas'),
	('third', 'Austin'),	
])

print(tx)

things = dict(
		hair = 'brown',
		eye = 'blue',
		glasses = 'yes',
		height = '5 ft 4 in')

print(things)

# Accessing elements
print(tx['second'])

# Adding elements
tx['four'] = 'San Antonio'
print(tx['four'])

# Edit elements
tx['four'] = 'Sugarland'
print(tx['four'])

# Delete elements
del tx['four']
print(tx)

d = {}
d['key'] = 'value'
d['3'] = 3
d['adict'] = {'one': 1, 'two': 2}

print(d)
print(type(d))
print(d['adict']['one'])

d[3.4] = 'Three something'
print(d)

# Restrictions
dc = {float: '3.4', int: '2', str:'String here', bool: True}
print(dc)

c = {'one': 1, 2: 'two', 2: 'three'}
print(c)

d = {(1, 2): 1, (2, 1): 2}
print(d)
print(d[(1, 2)])

# No restriction on Values

d = {1: 1, 2: 1, 'one': 1}
print(d)

# Built-in Functions in Dictionaries (and Operators)
tx = dict([
	('one', 'Houston'),
	('second', 'Dallas'),
	('third', 'Austin'),	
])

# in / not in
print('four' in tx)
print('one' not in tx)

# tx['four']
print('four' in tx and tx['four'])

# len()
print(len(tx))

# clear()
tx.clear()
print(tx)

tx = dict([
	('first', 'Houston'),
	('second', 'Dallas'),
	('third', 'Austin'),	
])

# get(<key>, <default>)
print(tx.get('one'))
print(tx.get('four', 'There is nothing to see here'))

# items()
print(tx.items())

# keys()
print(tx.keys())

# values()
print(tx.values())

# pop(<key>, <default>)
print(tx.pop('third'))
print(tx.pop('third', False))

# popitem()
print(tx)
print(tx.popitem())

print(tx)

# update()
dict1 = {1: 'a', 2: 'b'}
dict2 = {3: 'c', 4: 'd'}

dict1.update(dict2)
print(dict1)

dict1.update(a = 1, b = 2)
print(dict1)

dict1.update([('a', 3), ('b', 4)])
print(dict1)

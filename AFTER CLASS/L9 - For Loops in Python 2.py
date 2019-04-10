"""
Lecture 9: For Loops in Python
Momentum Learning
Introduction to Python
M. Bedir Tapkan
"""

# Numerical Range
# for i = 1 to 10:
# 	<code>

# for <var> in <iterable>:
# 	<statement(s)>

a = ['a', 'b', 'c']
for i in a:
	print(i)

# iter()
print(iter("My Name"))
print(iter(['a', 1]))
print(iter((1, 2, 3)))
print(iter({'a': 1}))
print(iter({'a', 'b'}))

a = ['a', 'b', 'c']
itr = iter(a)
print(itr)

print(next(itr))
print(next(itr))
print(next(itr))

# next(itr)

itr2 = iter(a)
print(next(itr2))

# Terms - Meaning
# ITERATION - 	The process of looping through
# 				the objects or items in a collection
# ITERABLE - 	An object that can be iterated over
# ITERATOR - 	The object that produces successive
#				items or values from its associated 
#				iterable
# iter() -		The function (built-in) to obtain an
#				iterator from an iterable

d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
	print(k)
	print(d[k])

for i in d.values():
	print(i)

# Unpack tuples - reminder
t = (1,2,3,4)
print(t)
print(type(t))
one, two, three, four = t
print(one)

t = [(1, 2), (3, 5), (4, 2), (6, 0)]
for i, j in t:
	print(i, j)

d = {'a': 1, 'b': 2, 'c': 3}
print(d.items())

for i, j in d.items():
	print("the key = ", i, " | the value = ", j)

for i in (0,1,2,3,4,5):
	print(i)

# range()
n = range(6)
print(n)
print(type(n))

for i in n:
	print(i)

# Write a loop that prints your name
# 100 times

for _ in range(100):
	print("Bedir")

# Write a loop that prints your name
# 10 times with the number in front.

for i in range(10):
	print(i+1, "Bedir")

# range(<start>, <end>, <step>)
for i in range(2, 18, 3):
	print(i)

# Alter the for Loop

# break
for i in range(10):
	if i == 5:
		break
	print(i)
# continue
for i in range(10):
	if i == 5:
		continue
	print(i)

# else-statement in for loop
for i in ['a', 'b', 'c']:
	print(i)
else:
	print("Done")

# Write a for loop that prints the number of elements
# left that are not printed + print the current element
n = 10
for i in range(n):
	print("Elements left= ", n-i-1 , " | current element = ", i)



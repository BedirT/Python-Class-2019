"""
Lecture 6: Lists & Tuples
Momentum Learning
Introduction to Python
M. Bedir Tapkan
"""

# -Left from last class:
# rpartition(<sep>)
print("Hi are we are here!".partition("are"))
print("Hi are we are here!".rpartition("are"))

# # split(sep=None, maxsplit=-1)
print("Hi,guys,we,are,here!".split(','))
print("Hi,guys,we,are,here!".split(',', maxsplit=3))

# # rsplit(sep=None, maxsplit=-1)
print("Hi,guys,we,are,here!".rsplit(',', maxsplit=3))

# # splitlines([<keepends>])
print("Hi guys\nwe are here!".splitlines())

# Python Lists
ls = ['student1', 'student2', 'teacher']
print(ls)

# Lists are ordered.
ls1 = ["Apple", "Orange", "Pear"]
ls2 = ["Apple", "Pear", "Orange"]
print(ls1 == ls2)
print(ls1 is ls2)

# Lists can contain any arbitrary objects.
ls = [1, 2, 3, 5]
print(ls)
ls = [1, 'Me', 2, 3.2, 5, 'Hey']
print(ls)

ls = [len, int, 'Me', 1]
print(ls)

# List elements can be accessed by index.
ls = [1, 2, 3, 4, 5]
print(ls[0])
print(ls[0:2])
print(ls[0::2])

print(ls[-1])
print(ls[::-1])

print(ls[:])
print(ls[:] is ls)

print(1 in ls)
print(6 in ls)
print(7 not in ls)

# + - Concatenate, * - Replicate
ls = [1, 2, 3, 4, 5]
ls = ls + [6, 7]
print(ls)

print(ls * 2)

# Create list 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1 
# - just using slicing and concatination
print(ls + ls[-2::-1])

# len
print(len(ls))

# min
print(min(ls))

# max
print(max(ls))

# sum
print(sum(ls))

# Lists can be nested to arbitrary depth.
ls = [ 	['Hi', 'Bedir', 3],
		[4, 5, 6],
		[7, 8, 9]	]

print(ls[0])
print(ls[0][1])
print(ls[0][1][0])
# print(ls[1])

print(len(ls))
print(len(ls[0]))

# Lists are mutable.
# Modifying a Single List Value
ls = [1, 2, 3, 4]
ls[2] = -1
print(ls)

# del
del ls[1]
print(ls)

# Modifying Multiple List Values
ls = [1, 2, 3, 4, 5, 6]
print(ls[1:3])
ls[1:3] = ['HEEEYY']
print(ls)

# adding new values
ls[1:2] = ['Here', 2, 'entries']
print(ls)

ls[2] = ['Two', 'Three']
print(ls)

# Prepending or Appending Items to a List

# Methods That Modify a List
# append

# extend

# insert

# remove

# pop(index=-1)

# Lists are dynamic.


# Python Tuples

# Tuple Assignment, Packing, and Unpacking

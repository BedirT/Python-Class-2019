"""
Lecture 7: Lists & Tuples Part 2
Momentum Learning
Introduction to Python
M. Bedir Tapkan
"""

# Prepending or Appending Items to a List
ls = ['a', 'b', 'c']
ls += ['d', 'f']
print(ls)

ls = ['a', 'b', 'c']
ls = ['d', 'f'] + ls
print(ls)

# You can't append one item, you have to append a list
# ls += 20 # Wrong
ls += [20]
print(ls)

# Methods That Modify a List
# append
# ls.append(<obj>)
ls = [1, 2, 3]
ls.append(4)
print(ls)

# We also can append a list
ls.append([5, 6])
print(ls)

# extend
# ls.extend(<obj>)
ls = [1, 2, 3]
ls.extend([5, 6])
print(ls)

# insert
# ls.insert(<index>, <obj>)
ls = [1, 2, 3]
ls.insert(1, 4)
print(ls)

# remove
ls = [1, 2, 3]
ls.remove(2)
print(ls)

# pop(index=-1)
ls = [1, 2, 3]
print(ls.pop())
print(ls)

ls = [1, 2, 3, 2, 5]
ls.pop(1)
print(ls)

# Lists are dynamic.
ls = [1, 2, 3, 2, 5]
ls[3] = 4
print(ls)

ls.remove(2)
print(ls)
# Python Tuples
t = ('a', 'b', 'c')
print(t)
print(type(t))

print(t[0])

print(t[0:2])
print(t[::-1])

# Unlike lists tuples are immutable
# t[0] = 'd'
t = (2)
print(t)
print(type(t))

t = (2,)
print(type(t))

# Tuple Assignment, Packing, and Unpacking
t = (1, 2, 3)
print(type(t))
t = 1, 2, 3
print(type(t))
t = 1,
print(type(t))

t = 1, 2, 3, 4
print(t)
print(type(t))
one, two, three, four = t
print(one)

# one, two, three = t
print(type(one))

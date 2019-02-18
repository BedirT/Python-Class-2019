"""
Lecture 4.2: Strings and Characters in Python: Part 1
Momentum Learning
Introduction to Python
M. Bedir Tapkan
"""

# Operators in Strings
# Concatination + 
name = "Bedir"
print(name)
name = name + " " + "Tapkan"
print(name)
print("M " + name)

# Multiply strings *
print("meh" * 5)

# in operator + not
print('B' in name)
print('B' not in name)

# Built-in String Functions
# chr()
# ASCII and Unicode
# a = chr(3)
# print(type(a))
# print(chr(30000))
### hw - all unicode table

# ord()
print(ord('a'))

# len()
print(len("My name is Bedir!"))

# str()
d = str(304)
print(304)
print(d)

print(type(304))
print(type(d))

# String indexing
nm = "Krithik"
print(nm[3])

print(nm[6])
print(nm[len(nm)-1])
# Negative indexes
print(nm[-1])

# Slicing
print(nm[1:4])
print(nm[1:])
print(nm[:4])
print(nm[1:-1])

# Stride (Steps)
print(nm[1::2])
print(nm[2::-1])
print(nm[4:0:-1])

# Interpolating Variables Into a String
a, b = 3, 4
print("a is", a, "and b is", b)

# f-strings
print(f"a is {a} and b is {b}")

# Modifying Strings - immutable
n = "Me"
# n[0] = 'N'
# replace ?
n = n.replace('M', 'N')
print(n)
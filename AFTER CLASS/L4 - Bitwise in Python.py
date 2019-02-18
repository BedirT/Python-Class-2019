# """
# Lecture 4.1: Bitwise in Python
# Momentum Learning
# Introduction to Python
# M. Bedir Tapkan
# """

# Bitwise Operators
# & - bitwise AND
print(0b101 & 0b010)
print(0b010 & 0b10111)

# | - bitwise OR
print(0b1111 | 0b0101)

# ~ - bitwise negation
print(~0b1010)

# ^ - bitwise XOR (exclusive OR)
print(0b1011 ^ 0b0110)

# >> - Shift right n places
print(10 >> 1)

# << - Shift left n places
print(10 << 1)
print(10 << 2)
print(10 << 3)
print(13 << 1)

# Identity Operators
# is
a = 300
print(id(a))
b = 300
print(id(b))
print(a is b)
print(a is 300)

# # is not
x = "hey"
print(id(x))
print(x is not a)

# Operator Precedence
# LEAST
# or
# and
# not
# Comparison (==, !=, <=, <, >=, >, is, is not)
# | - Bitwise or
# ^ - Bitwise XOR
# & - Bitwise and
# <<, >> - Bitwise Shift
# +, -
# *, /, //, %
# +x, -x, ~x
# **
# MOST

print(3 + 5 * 2)
print(2 < 3 and 10 > 30)

# Augmented Assignment Operators
a = 5
a = a * 2
print(a)
# """
# Lecture 3.2: Operators and Expressions in Python
# Momentum Learning
# Introduction to Python
# M. Bedir Tapkan
# """

# # Arithmetic Operators
# num1 = 3
# num2 = 8

# # Addition
# # +
# addition = num1 + num2
# print(addition)

# print(5 + 34 + 2 + 3)

# # Substruction
# # -
# subs = num1 - num2
# print(subs)

# # Multiplication
# # *
# mul = num1 * num2
# print(mul)

# # Division
# # /
# div = num1 / num2
# print(div)

# # Modulo
# mod = num2 % num1
# print(mod)

# # Floor Division (also called Integer Division)	
# # Quotient when a is divided by b, rounded to
# # the next smallest whole number
# # //
# divFloor = num2 // num1
# print(divFloor)

# # Exponentiation
# # **
# exp = num2 ** num1
# print(exp)
# print(pow(num2, num1))

# # Comparison Operators
# # Equal to
# # ==
# print(num1 == num2)
# print(3 == 3)

# # # Not equal to
# # # !=
# print(num1 != num2)
# print(3 != 3)

# # Less than
# # <
# print(num1 < num2)
# print(4 < 3)

# # Less than or equal to
# # <=
# print(num1 < num2)
# print(4 < 3)

# # Greater than
# # >
# print(num1 < num2)
# print(4 < 3)

# # Greater than or equal to
# # >=
# print(num1 < num2)
# print(4 < 3)


# # Equality Comparison on Floating-Point Values
# a = 3.1
# b = 5.1
# print(a)
# print(b-2)
# print(a == b-2)

# # Logical Operators
# # not
# n1 = True
# n2 = False
# print(not n1)
# print(not False)

# # or
# marker1 = "blue"
# marker2 = "orange"
# marker3 = "red"
# print(marker3 == "blue" or marker2 == "blue")

# # # and
# marker4 = "blue"
# print(marker1 == "blue" and marker4 == "blue")

# # Evaluation of Non-Boolean Values in Boolean Context
# # Numeric Value
# print(bool(0))
# print(bool(1))

# print(bool(0.00))
# print(bool(0.1))

# # String
# print(bool(""))
# print(bool("0"))

# # Built-In Composite Data Object
# print(type([]))
# print(bool([]))
# print(bool([3, 4, 5]))

# # # The “None” Keyword
# print(bool(None))
 
# # Logical Expressions Involving Non-Boolean Operands
# # “not” and Non-Boolean Operands
# print(not 0)

# # # “or” and Non-Boolean Operands
# print(0 or 3)

# # # “and” and Non-Boolean Operands
# print(0 and 3)
# print(4 and 3)


# # Bitwise Operators
# # & - bitwise AND
# print(0b101 & 0b010)
# print(0b010 & 0b10111)

# # | - bitwise OR
# print(0b1111 | 0b0101)

# # ~ - bitwise negation
# print(~0b1010)

# # ^ - bitwise XOR (exclusive OR)
# print(0b1011 ^ 0b0110)

# # >> - Shift right n places
# print(10 >> 1)

# # << - Shift left n places
# print(10 << 1)
# print(10 << 2)
# print(10 << 3)
# print(13 << 1)

# Identity Operators
# is
# a = 300
# print(id(a))
# b = 300
# print(id(b))
# print(a is b)
# print(a is 300)

# # is not
# x = "hey"
# print(id(x))
# print(x is not a)

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

# print(3 + 5 * 2)
# print(2 < 3 and 10 > 30)

# Augmented Assignment Operators
a = 5
a = a * 2
print(a)

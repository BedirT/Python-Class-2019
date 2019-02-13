# """
# Lecture 3: Variables in Python
# Momentum Learning
# Introduction to Python
# M. Bedir Tapkan
# """

# # Variable Assignement
n = 400
myname = "Bedir"

print(myname)

imfloat = 500.
print(type(imfloat))

# Chained Var Assignment
a = b = c = 200

# Variable Types in Python
number1 = 3
print(type(number1))

number1 = "Melody"
print(type(number1))

a = 5.0
print(type(a))

a = int(5.0)
print(type(a))

# Object References
n = 300
print(n)

# Multi References
m = n
print(m)

# Garbage Collection
n = 400
m = "Hi"

# Object Identity
n = 300
print(id(n))
m = 300
print(id(m))
m = 400
print(id(m))

a = 5000
b = 5000
print(id(a))
print(id(b))

# Variable Names
name = "Bob"
Age = 54
has_W2 = True
print(name, Age, has_W2)

1099_filed = False
# Not valid - Variables cannot start with numbers

# Camel Case
hiHouston = "Hi Houston!"

# Pascal Case
HoustonRockets = "Houston Rockets"

# Snake Case
this_is_number = 3

# Reserved Words (Keywords)
# We have 33 Keywords
for = 3
# Not valid

# INDENTATION
 a = 2
# Not valid! If the indentation is wrong, you will get Indentation error.

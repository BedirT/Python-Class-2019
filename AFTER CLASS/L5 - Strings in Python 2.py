"""
Lecture 5: Strings and Characters in Python
Momentum Learning
Introduction to Python
M. Bedir Tapkan
"""

# Built-in String Methods
# Invoking methods .
# obj.methodName(<args>)

s = "bedir TaPKan"

# Case Conversion
# capitalize
print(s.capitalize())

# lower
print(s.lower())

# swapcase
print(s.swapcase())

# title
print(s.title())

# upper
print(s.upper())

# Find and Replace
# count(<sub>[, <start>[, <end>]])
s1 = "Whats on TV tonight?"
s2 = "on"
print(s1.count(s2))
print(s1.count(s2, 10))
print(s1.count(s2, 10, 14))

# endswith(<suffix>[, <start>[, <end>]])
s1 = "Hi how are you"
s2 = "you"
print(s1.endswith(s2))
print(s1.endswith(s2, 12))
print(s1.endswith(s2, 4, 13))

# startswith(<prefix>[, <start>[, <end>]])
s1 = "Life is good!"
s2 = "Life"
print(s1.startswith(s2))
print(s1.startswith(s2, 2))
print(s1.startswith(s2, 0, 3))

# find(<sub>[, <start>[, <end>]])
s1 = "Karthic is the best!"
s2 = "the"
print(s1.find(s2))
print(s1[11])
print(s1.find(s2, 12)) # he best!
print(s1.find(s2, 0, 13)) # Karthic is th

# index(<sub>[, <start>[, <end>]])
# print(s1.index(s2, 12)) # he best!

# rfind(<sub>[, <start>[, <end>]])
s1 = "Hey, this word is this world!"
s2 = "this"
print(s1.find(s2))
print(s1.rfind(s2))

# rindex(<sub>[, <start>[, <end>]])
print(s1.rindex(s2))


# Character Classification
# isalnum()
s1 = "Haha35"
print(s1.isalnum())

# isalpha()
s1 = "Bedir"
print(s1.isalpha())

# isdigit()
s1 = "30"
print(s1.isdigit())

# isidentifier()
print("0hime".isidentifier())
print("hi me".isidentifier())
print("hiMe".isidentifier())
print("hi_me".isidentifier())

print("for".isidentifier())

# isprintable()
print("Hi this\nis me!".isprintable())
print("Hi this is me!".isprintable())

# isspace()
print("  \n \t".isspace())

# islower()
print("is it lower?".islower())
print("Or no?".islower())

# istitle()
print("Bedir Tapkan".istitle())

# isupper()
print("I am coding?".isupper())
print("Bedir".upper().isupper()) # Chaining the methods

# String Formatting
# center(<width>[, <fill>])
print("M".center(20, '-'))
print("Bedir".center(20))
print("Tapkan".center(20))
print("Momentum Learning".center(20))

# expandtabs(tabsize=8)
print("I\tlove\tthis!".expandtabs(tabsize=16))

# ljust(<width>[, <fill>])
print("Bedir".ljust(20, '-'))

# rjust(<width>[, <fill>])
print("Bedir".rjust(20, '-'))

# lstrip([<chars>])
print("   bedir hi ".lstrip())

# rstrip([<chars>])
print("   bedir hi      ".rstrip())

# strip([<chars>])
print("   bedir hi      ".strip())
print("http://www.momentumlearning.org".strip('htp:/grow.'))

# replace(<old>, <new>[, <count>])
print("Go to school.".replace('school', 'home'))

# zfill(<width>)
print('50'.zfill(10))
print('-50'.zfill(10))


# Converting Between Strings and Lists
# join(<iterable>)
print(', '.join(['They', 'We', 'Us']))
print('-'.join(['I', 'They', '30', '50']))

# partition(<sep>)
print("Hi guys we are here!".partition("guys"))

# rpartition(<sep>)

# split(sep=None, maxsplit=-1)

# rsplit(sep=None, maxsplit=-1)

# splitlines([<keepends>])


# bytes Objects

b = b'hereweare12'

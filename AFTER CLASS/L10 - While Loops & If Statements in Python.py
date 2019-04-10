"""
Lecture 10: While Loops and If-Else in Python
Momentum Learning
Introduction to Python
M. Bedir Tapkan
"""

# while <condition>:
#	<statement(s)>

# ex
n = 5
while n > 0:
	n -= 1
	print(n)

# ex
a = [1, 2, 3]
while a:
	print(a.pop())

n = 5
while n > 0:
	n -= 1
	if n == 2:
		continue
	print(n)

# while <condition>:
# 	<statement>
# else:
# 	<other_statements>

#infinite loop
# while True:
# 	print("HI!")

# if-else Statements

# if <condition>:
# 	<statement>

a = 0
b = 1

if a < b:
	print("Yes, it is smaller!")

if b > a:
	print("No, it is greater!")

if a and b:
	print("Done - and")

if a or b:
	print("Done - or")

if 'd' in 'Bedir':
	print("Done - in it")

# If the weather is nice I will:
# 	- Mow the lawn
# 	- Weed the garden
# 	- Take the dog for a walk
# If the weather is not nice then I won't do any of these

if True:
	a = 4
	b = 2

a = 3
b = 0
if a > 0:
	if b > 0:
		print("Success!")
	else: 
		print("b just failed!")	
else:
	print("Failure!")

if a == 1:
	print('One')
if a == 2:
	print('Two')
if a == 3:
	print('Three')

a = 7
if a > 5:
	print("Yes")
elif a < 8:
	print("No")
elif a == 3:
	print("Interesting!")
else:
	print("No idea")

# pass
if a == 7:
	pass

print('Hey')

a = 17

if a > 15:
	print("1")
elif a > 14:
	print("2")
elif a > 10: 
	print("3")
else:
	print('4')
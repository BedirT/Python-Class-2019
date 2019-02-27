# Homework

### Week 2

Convert ```1010``` in hexadecimal to its 10th base by using pythons in-place functions ```pow()``` and ```sum()```.

**Tip:** You can use ```0x``` to verify your solutions

**Answer:**

```python
print(sum([pow(16,0)*0, pow(16,1)*1, pow(16,2)*0, pow(16,3)*1]))
# Result: 4112

# To verify
print(0x1010)
# Result: 4112
```

### Week 3

1- From the given values to three string variables that have values - ‘Small’, ‘Medium’, ‘Large’, and then write the code that prints the truth value of each one being ‘Small’.

2- Create two variables ```a, b```; that have integer values ```3, 7```. 
  - Multiply them with each other, store the result in another variable. 
  - Add ```4a```’s to the result. 
  - Get the remainder of the result divided by ```b```.
  - Print the truth value of the end result being greater than or equal to ```a``` and ```b``` separately.

***PS: Print after every line.***

**Answer:**

```python
# Question 1:
strS = 'Small'
strM = 'Medium'
strL = 'Large'

print(strS == 'Small')
print(strM == 'Medium')
print(strL == 'Large')

# Question 2:
# part 1
a, b = 3, 7
c = a * b
print("a * b =", c)
# part 2
c = c + 4 * a
print("c + 4a =, c)
# part 3
c = c % b
print("c % b =", c)
# part 4
print(c >= a)
print(c >= b)
```


### Week 4

1. Write a program that gets an integer input from user and prints the corresponding Unicode character.
2. Write a program that first gets a string from user and second shorter one, and print the truth value of - if the second string is included in the first one. (DO NOT use if statements or any other conditionals, we learned a method to achive this.)
3. Write a program that gets a string from user and prints the length of it.
4. Write a program that cuts a string from user and gets 3 integers:
  - Start point
  - End point
  - What is the step size (we specified in class)
  
```python
# Q1
num = input("Enter a number to check the corresponding unicode character: ")
print("The corresponding unicode character is ", chr(int(num)))

# Q2
s1 = input("Please enter the first string: ")
s2 = input("Please enter a string to search in s1: ")
print(s2 in s1)

# Q3
s = input("Please enter a string to check the size of it: ")
print("The size of the string is ", len(s))

# Q4 
s = input("Please enter a string to test the substring: ")
start = int(input("Please enter an integer, it will indicate the starting index for the substring: "))
end = int(input("Please enter an integer, it will indicate the end index for the substring: "))
step = int(input("Please enter an integer, it will indicate the step size for creating the substring: "))
print(s[start:end:step])
```


### Week 5

Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

**Sample String:**
- 'The lyrics is not that poor!'
- 'The lyrics is poor!'

**Expected Result:** 
- 'The lyrics is good!'
- 'The lyrics is poor!'

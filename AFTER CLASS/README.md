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


### Week 4

1- Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

**Sample String:**
'The lyrics is not that poor!'
'The lyrics is poor!'
**Expected Result:** 
'The lyrics is good!'
'The lyrics is poor!'

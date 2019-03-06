# s1 = "He is not that poor"
s1 = input("Enter the phrase: ")
print(s1)
s1 = s1.replace(s1[s1.find('not'):s1.find('poor')+len('poor')+1], 'good')

print(s1)


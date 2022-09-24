''' 
2 types of Collection 
    i.  Lists - A linear collecttion of values that stay in order
    ii. Dictionary - A bag of values each with its own label

Dictonaries are python's most powerful collection
- Associative array - Perl / Php
- Properties or Map or HashMap - Java
- Property Bag - C# / .Net
'''

'''
Purse example
'''
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

'''Comparing Lists and Dictionaries
Dictonaries are like lists except they use 'keys' instead of
numbers to look up 'values' 
They have "key : value" pairs 
Empty dictonary -- '''
empty = { } 
print(empty)
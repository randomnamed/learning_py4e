'''
Rgular expressions are really clever "wild card" 
expressions for matching and parsing strings
'''
'''
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
'''
import re

x = 'My 2 faourite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+',x)
print(y)

# Greedy matching
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)
# Non-Greedy matching
y = re.findall('^F.+?:',x)
print(y)

#Fine-tuning String Extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print('Fine-tuning',y)
#Parantheses are not part of the match - but they tell where
#to start and stop what string to extract
y = re.findall('^From (\S+@\S+)',x)
print('Parantheses',y)

# Normal split data
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

#Double Split pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#Regex Version
y = re.findall('@([^ ]*)',data)
#  []-match non-bklank character *-Match many of them
print(y)

#Even Cooler Regex Version
y = re.findall('^From .*@([^ ]*)',data)
# ^-Starting at the beginning of the line, look for the string 'From'
print(y)

#Spam Confidence
hand = open('code3/mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    #print(stuff)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    #print(num)
    numlist.append(num)
print('Maximum:', max(numlist))

#Escape Character
#Use '\' to use special character as a normal string
x = 'We just received $10.00 for cookies'
y = re.findall('\$[0-9.]+',x)
# \$ - A real dollar sign [0-9.]-A digit or period +-At least one or more
print(y)

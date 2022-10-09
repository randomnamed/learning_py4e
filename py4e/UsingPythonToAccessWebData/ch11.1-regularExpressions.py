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

hand = open('code3/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('^From:', line):
    #    print(line)
    #if re.search('^X.*:', line):
    #    print(line)
    if re.search('^X-\S+:', line):
        print(line)

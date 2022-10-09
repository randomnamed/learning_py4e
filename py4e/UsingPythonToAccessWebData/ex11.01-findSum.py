'''
Finding Numbers in a Haystack

In this assignment you will read through and parse 
a file with text and numbers. You will extract 
all the numbers in the file and compute the sum of the numbers.
'''
'''
Handling The Data
The basic outline of this problem is to read the file, 
look for integers using the re.findall(), 
looking for a regular expression of '[0-9]+' 
and then converting the extracted strings to integers 
and summing up the integers.
'''
import re

#hand = open('py4e/UsingPythonToAccessWebData/sample.txt')
#hand = open('py4e/UsingPythonToAccessWebData/regex_sum_42.txt')
hand = open('py4e/UsingPythonToAccessWebData/regex_sum_1638415.txt')
answer = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    #print(stuff)
    #if len(stuff) != 1 : continue
    for i in stuff:
        num = int(i)
        #print(num)
        answer = answer + num
print('Final Sum:', answer)

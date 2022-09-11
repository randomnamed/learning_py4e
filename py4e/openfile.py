# FILE HANDLE
'''
Input and Output Devices <-> Software <-> Secondary Memory
Input and output - Reading Inputs and printing Outputs
Software consists of - < CPU & Main Memory >
Main memory - Holds the programming code
Secondary memory - This holds the Files
'''
'''
A text file is a sequence of lines
\n is for new lines
Enter button is also '\n' for the computer
New lines are white space
print function puts new line automatically || There are ways of telling it not to do it as well
'''

# What is Handle ? - Open, Read, Write, Close
# When Files are missing - Traceback is printed 'No such file found'
# ** handle = open(filename,mode) **
# returns handle use to manipulate the file
# filename is a string
# mode is optional and can be 'r' for read and 'w' for writing to the file
'''
fhand = open ('../code3/mbox.txt','r')
print(fhand)
'''

'''
xfile = open ('../code3/mbox.txt')
for cheese in xfile:
    print(cheese)
'''
# File length / Line counter
'''
fhand = open('../code3/mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)
'''

# Read the Whole file
'''
fhand = open('../code3/mbox-short.txt')
inp = fhand.read()
print(len(inp)) # returns number of characters in the file
print(inp[:20]) # starting from 0 to 20 so these are first 20 characters
'''
# Searching through the file & rstrip() to remove whitespaces
'''
fhand = open('../code3/mbox-short.txt')
for line in fhand: # Read line by line
    line = line.rstrip() # this will strip whitespaces
    if line.startswith('From: ') :
        print(line) # print statement will add new \n line -- so we use "rstrip()" to strip the whitespaces
'''
# Skiipping with Continue (This can do the same as above code to skip the bad lines)
'''
fhand = open('../code3/mbox-short.txt')
for line in fhand:
    line = line.rstrip() # this will strip whitespaces
    if not line.startswith('From: ') :
        continue
    print(line) 
'''

# Using 'in' to select lines
'''
fhand = open('../code3/mbox-short.txt')
for line in fhand:
    line = line.rstrip() # this will strip whitespaces
    if not '@uct.ac.za' in line :
        continue
    print(line) 
'''

# Prompt for File name and counting (Handling BAD file names)
fname = input('Enter the file name: ')
try:
    fhand = open('../code3/'+ fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject line in', fname)
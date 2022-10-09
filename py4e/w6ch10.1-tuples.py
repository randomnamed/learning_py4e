# Tuples are unmodifiable/immutable list
# Tuples are efficient so used as temporary variables

#List example
l = list()
dir(l)
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
xlist = [9, 8, 7]
xlist[2] = 6
print(xlist)

#Tuple example
t = tuple()
dir(t)
# ['count', 'index']
x = ('Glenn', 'Sally', 'Joseph')
y = (1, 9, 2)
#y[2] = 1 TypeError: 'tuple' object does not support item assignment
print(x[2]) ;'''indexing'''
print(y)
print(max(y))
for iter in y:
    print(iter)

(xx, yy) = (4, 'fred')
print(yy)

'''
Tuples are comparable
If the first is equal then it goes to next until it finds element that differ
'''
compare1 = (0,1,2) < (5,1,2)
print(compare1)
#compare2 = (0,1,2000) < (0,3,4)
#print(compare2)
#compare3 = ('Jones','Sally') < ('Jones','Sam')
#print(compare3)
#compare4 = ('Jones','Sally') > ('Adam','Sam')
#print(compare4)

'''
Sorting Lists of Tuples 
sort dictionary by the key using 'items()' method and sorted() function
same key is not possible more than once
'''
d = {'a':10, 'c':22, 'b':1}
print(d.items())
print(sorted(d.items()))

'''
Using sorted()
We can do this even more directly using the 
built-in function 'sorted' that takes a sequence as a parameter
and returns a sorted sequence
'''
for k,v in sorted(d.items()):
    print(k,v)

'''
Sort by Values instead of Key
-If we could construct a list of tuples of the form
 (value,key) we could sort by value
-We do this with a for loop that creates a list of tuples
'''
tmp= list()
for k,v in d.items():
    tmp.append( (v,k) ) # reversing the tuples individually
print(tmp) # gives list of tuples
tmp = sorted(tmp, reverse=True) # for big to small sorting
print(tmp)

'''
Th top 10 most common words
'''
fhand = open('code3/romeo.txt') # open file
counts = dict() # make dictionary
for line in fhand: # loop throuhg lines of file
    words = line.split() # split the words in the file
    for word in words: # loop though the words in the file
        counts[word] = counts.get(word, 0) + 1
# Histogram is build at the end of the above code
lst = list() ;'''-----start'''
for key,val in counts.items(): 
    newtup = (val,key) # reversing the value key tuple here
    lst.append(newtup)

lst = sorted(lst, reverse=True) # big to small sorted list of tuple

for val,key in lst[:10] : # slicing goes from 0 to 9
    print(key,val) ;'''-----end in one line''' # reverse to key value again and print

'''Even Shorter Version
"List Comprehension" creates dynamic list. we make a reverse tuple and then sort it.
'''
print( sorted ( [ (v,k) for k,v in d.items() ] ) )
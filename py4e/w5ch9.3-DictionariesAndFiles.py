''' 
counting Pattern
'''
# counts = dict()
# print('Enter a line of text:')
# line = input('')
# 
# words = line.split()
# print('Words:', words)
# 
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word,0) + 1 # this does the new and exisitig addition
# print('Counts', counts)

'''
Difinite Loops and Dictionaries
'''
# counts = {'chuck':1, 'fred':42, 'jan':100}
# for key in counts :
#     print(key, counts[key])
# print(list(counts))
# print(counts.keys())
# print(counts.values())
# print(counts.items())  

'''key-value pair in dictionary using 2 iteration variables
each Iteration is 1st - key and 2nd - value for the key'''
# for aaa,bbb in counts.items():
#     print(aaa, bbb)

'''Part 3'''
name = input('Enter file: ')
handle = open('code3/'+ name)

counts = dict()
for line in handle: # runs for every line of the file
    words = line.split() # gives each word in each line
    for word in words: # goes through each word
        counts[word] = counts.get(word,0) + 1 # adds new words / counts them (histogram)
# inside counts variable we have all the count for all the words in the file 
bigcount = None
bigword = None
for word,count in counts.items(): # goes through all the "key, value" in word,count
    if bigcount is None or count > bigcount: # max count logic
        bigword = word
        bigcount = count

print(bigword,bigcount)
stuff = dict()
print(stuff.get('candy',-1))
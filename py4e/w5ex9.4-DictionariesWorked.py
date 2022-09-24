''' 
9.4 Write a program to read through the mbox-short.txt 
and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of 
those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the 
sender's mail address to a count of the number of times they 
appear in the file. 
After the dictionary is produced, 
the program reads through the dictionary using a 
maximum loop to find the most prolific committer.
'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open('code3/'+ name)

di = dict()
emailIds = ''
for lin in handle: # runs for every line of the file
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split() # gives each word in each line
    # print(wds)
    for w in wds: # goes through each word
        # # print(w)
        ''' if the key is not there the count is zero'''
        # oldcount =  di.get(w,0)
        # print(w,'old',oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w,'new',di[w])
# print(di)
        #print(w, di[w])
'''now we want to find the most common word'''
largest = -1
theword = None
for k,v in di.items() :
    # print(k,v)
    if v > largest :
        largest = v
        theword = k # capture / remember the word that was largest
print(theword,largest)
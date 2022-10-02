'''
10.2 Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day 
for each of the messages. 
You can pull the hour out from the 'From ' line 
by finding the time and then splitting the 
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below.
'''
name = input("Enter file:")
if len(name) < 1:
    name = "clown.txt"
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
        '''idiom: retrieve/create/update counter'''
        di[w] = di.get(w,0) + 1
        #print(w,'new',di[w])
#print(di) # dictionary data

# x = sorted(di.items())
# print(x)

tmp = list()
for k,v in di.items():
    #print(k,v)
    newt = (v,k)
    tmp.append(newt)
#print('Flipped',tmp)

tmp = sorted(tmp)
#print('Sorted',tmp)
for v,k in tmp :
    print(k,v)
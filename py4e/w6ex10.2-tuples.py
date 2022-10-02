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
    name = "mbox-short.txt"
handle = open('code3/'+ name) # open file


di = dict() # make dictionary

for line in handle: # runs for every line of the file
    if "From" in line:
        words = line.split() # gives each word in each line
        if len(words) > 2:
            #print(words[5])
            word = words[5].split(":")
            hours = word[0]
            #print(hours)
            di[hours] = di.get(hours, 0) + 1
#print(di)
# Histogram is build at the end of the above code
lst = list()
for key,val in di.items(): 
    newtup = (key, val) # saving it in a new temp variable
    #print(newtup)
    lst.append(newtup)
lst = sorted(lst) 
#print(lst)  
for key,v in lst :
    print(key,v)
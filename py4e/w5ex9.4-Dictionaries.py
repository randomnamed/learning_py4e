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

counts = dict()
emailIds = ''
for line in handle: # runs for every line of the file
    words = line.split() # gives each word in each line
    for word in words: # goes through each word
        if word == 'From':
            emailIds = words[1]
            counts[emailIds] = counts.get(emailIds,0) + 1 # adds new words / counts them (histogram)
# inside counts variable we have all the count for all the words in the file 
bigcount = None
bigword = None
for word,count in counts.items(): # goes through all the "key, value" in word,count
    if bigcount is None or count > bigcount: # max count logic
        bigword = word
        bigcount = count

print(bigword,bigcount)
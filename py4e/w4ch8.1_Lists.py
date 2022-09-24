# Algorithms - A set of rules
# Data Structures - A particular way of organizing data
# list dictornaries and tuples

# Concatination
'''
a = [1 ,2, 3, 77, 12]
b = [4, 5, 6]
c = a + b
#print(c)
#print(a)
# Slicing
a[1:3]
a[:3]
a[3:]
a[:]
'''
# average working
'''
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)
'''
#fhand = open('../code3/mbox-short.txt')
#for line in fhand:
#    line = line.rstrip()
#    if not line.startswith('From ') : continue
#    words = line.split()
#    print(words[2])
fhand = open('../code3/mbox-short.txt')
for line2 in fhand:
    line2 = line2.rstrip()
    print(line2)
    words = line2.split()
    print(len(words))
    x = (range(len(words)))
    print(x)
    print(x[2])
    print(words)
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])
    if line2.startswith('From ') : break

fruit = 'Banana'
fruit[0] = 'b'
print(fruit)
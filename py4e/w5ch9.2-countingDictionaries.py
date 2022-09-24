''' 
counting
'''

'''
count example
'''
# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1

# print(ccc)

# ccc['cwen'] = ccc['cwen'] + 1
# print(ccc)

'''Dictionaries Tracebacks
Error to reference key which is not in the dictionary
Use "in" operator to see if a key is in the dictionary
'''
# ccc = dict()
# print(ccc['csev'])
# 'csev' in ccc

'''When we see a new Name
'''
# counts = dict()
# names = ['csev','cwen','csev','zqian','csev']
# for name in names :
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts) 

# if name in counts:
#     x = counts[name]
# else:
#     x = 0

# x = counts.get(name, 0)
'''When we see a new Name
Simplified counting with get()
'''
counts = dict()
names = ['csev','cwen','csev','zqian','csev']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
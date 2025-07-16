movie = 'The Hunted'
print(movie[0]) # T
print(movie[1]) # h
print(movie[4]) # H
print(movie[-1]) # d
print(movie[-3]) # t


# print('Python'[7]) # string index out of range

# len - to find the length
print(len('Python'))

s1 = 'I am learning Python programming'
n = len(s1) # calculates the length of the string s1
print(s1[n-1]) # g

# string in python are immutable
# we have to make another variable to change it
print(s1[0])
s1[0] ='x' # 'str' object does not support item assignment
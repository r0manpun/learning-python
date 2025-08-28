# Data Structure - It represents a specialize format for organizing, processing, retrieving and storing data.

# List - variable that stores multiple values within it.
# In other programming languages, this data structure is called an array or vector.

# PYTHON LISTS
# to declare a list we use a pair of square brackets [] and between the square we put the
# elements/values with comma between them.
# List is an ordered sequence or collection of items.
# It can hold any datatype; integers, floats, strings, or booleans, even other lists, tuples, dictionaries.

l1 = [1, 2.5, 'python', True, ['abc','xyz'], (10,20,30)]

# ['abc','xyz'] - another list
# (10,20,30) - tuples

# to know length or how many items are there in a list
print(len(l1)) # 6

# empty list
l2 = []
l3 = list()

# We can refer any the elements/items in the list by using its index number.
print(l1[0]) # first element of l1 : 1
# we can also store it into a variable

# just as with strings, we can use negative indices to count from right to left.
x = l1[-1]
print(x) # (10,20,30)

# If we try to access an element that does not exist, we will get an index out of range error.
# print(l1[10]) #list index out of range

# String is immutable, it can't be changed.
s1 = 'xyz'
# s1[0]= 'X' # 'str' object does not support item assignment

# List is mutable, so it can be changed
l4 = list('abcd')
print(l4) # ['a', 'b', 'c', 'd']
print(id(l4)) # address of list l4 in the memory

l4[0] = 'X'
l4.append(100) # ['X', 'b', 'c', 'd', 100]
print(l4)
print(id(l4)) # same as before
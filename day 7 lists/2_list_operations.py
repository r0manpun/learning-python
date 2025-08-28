# LIST CONCATENATION

l1 = [3,4]
print(l1, id(l1)) # [3, 4] 4364007168

# concatenating the list
l1 = l1 + [5,6]
print(l1, id(l1)) # [3, 4, 5, 6] 4364213376

# Here,it doesn't change the previous list 'l1' but completely creates a new list 'l1' with different memory address

# If we want to concatenate to initial list and not create a new one, use plus equal.

l1 += [7,8]
print(l1, id(l1)) # [3, 4, 5, 6, 7, 8] 4299627648
# we can get same result with extend method.
l1.extend([11,12])
print(l1, id(l1))  # [3, 4, 5, 6, 7, 8, 11, 12] 4334050432

# Adding to the list. Two methods append and extend.
# Append - adds a single item to the end of the list
# Extend - extends the list by appending all the items from an iterable.

l1.append(['a', 'b'])
print(l1) # [3, 4, 5, 6, 7, 8, 11, 12, ['a', 'b']]
l1.extend(['x','y'])
print(l1) # [3, 4, 5, 6, 7, 8, 11, 12, ['a', 'b'], 'x' ,'y']
# extend appended all the items of the iterable to the end of the list.

# If we want to add a single item to the end of the list, we can either call the append method with that item
# or call the extend method with a list that has only that element.
# l1.append(20) # or
l1.extend([20])
# these two lines do the same thing
print(l1) # [3, 4, 5, 6, 7, 8, 11, 12, ['a', 'b'], 'x', 'y', 20]

# Extend method takes an iterable as an argument.
# l1.extend(20) # Error: object is not iterable
# here 20 is not an iterable


# Repetition
# we can repeat a list like a string using the star operator.
l2 = list('abc')
l3 = l2 * 3 # it repeats l2, 3 times
print(l3) # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

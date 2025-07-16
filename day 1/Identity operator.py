# Identity Operators: 'is' and 'is not'

# they don't compare the values stored in variables but the memory address referenced by the variables

a, b = 3,4
print(a is b) # returns True if they are both in same memory address otherwise False

# Mutability vs Immutability
# The value of a mutable variable can be changed after it has been created, but the value of an immutable variable can't be changed

# Immutable Types: int, float, string, tuple, frozenset
# Mutable Types: list, set, dict

# Immutable example
print(id(a)) # id of a or memory address where a settles
a+=3
print(a)
print(id(a)) # creates new memory address


# Mutable example
numbers = [1,2,3,4,5]
print(id(numbers))
numbers.append(100)
print(numbers)
print(id(numbers))

nums= numbers.copy()
print(nums == numbers)
print(id(nums)) # different memory address
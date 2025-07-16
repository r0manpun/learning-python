# TYPES in Python
# Numbers: int, float, complex;
# Booleans: True, False;
# Strings: language = "python";
# List and Tuples: cities = ['Kathmandu','Pokhara','Baglung'];
# Sets: states = {'CA','NY','DC'};
# Dictionaries: friend = {'name':'Luffy','age':20,'location':'Skypiea'}


# booleans
age = 20
name = 'Zoro'
# print(age==20) # true
# print(age>40) # false
# print(name == 'Zoro') # true
# print(len(name)!=10) #

# Note: in python there is a constant called 'None'
# this is frequently used to represent the absence of a value as some arguments are not based to a function
# or when function does not explicitly return something it returns 'None'


# Lists : ordered mutable sequences of objects
# - can contain any type of element
person = ['Roman', 24, 5.6, True, [1,2,3]]
# print(person)

# Tuples : ordered immutable sequences of objects

# Sets : mutable collection of unordered unique objects with no duplicate elements.
basket = {'apple', 'orange','apple', 'banana','orange'}
# print(basket) # show that duplicates have been removed
# {'apple','orange','banana'}

# set operations on unique letters from two words
a= set('abracadabra')
b=set('alacazam')
# print(a) # unique letters in a
# print(a - b) # letter in a but not in b
# print(a | b) # letters in a or b or both (a u b)
# print(a & b)  # letters in both a and b (a n b)

# Rower Sets : immutable collection of unordered unique objects

# Dictionaries : collection of unordered key-value data pair
tel = {'jack':4400,'fruit':3242}
tel['happy'] = 4221
# print(tel)
# {'jack': 4400, 'fruit': 3242, 'happy': 4221}

# dict() constructor builds dictionaries directly form sequences of key-value paris
items= dict([('soap',123),('biscut', 333),('orange', 123)])
print(items)



# Write a Python script to get a string made of the first 2 and last 2 chars from a given string entered by user.
my_str = 'Hello! Roman'
print(my_str[:2]+my_str[len(my_str)-2:]) # Gets a string made of the first and last 2 chars from a given string.

# Given solution
input_str = input('Enter a string(min 2 chars): ')
new_str = input_str[:2] + input_str[-2:]
print(new_str)
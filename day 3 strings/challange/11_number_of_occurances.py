# Write a Python script that finds the number of occurrences of a substring in a given string by ignoring the letter case.

s1 = 'I am learning Python programming'
new_str = s1.replace(' ','').lower()
print(len(new_str))

s2 = 'I am love Python'
new_str = s2.replace(' ','').lower()
print(len(new_str))

# Note: I didn't read the question properly and so i didn't understand the correct answer

# Given solution
my_str = "Welcome to Romania. romania is an awesome country, isn't it? Hello romania!"
sub_string = "Romania"

# Convert strong in lowercase.
tmp_str = my_str.lower()

# use the count function
count = tmp_str.count(sub_string.lower())
print(f'The substring "{sub_string}" appears {count} times in the string.')

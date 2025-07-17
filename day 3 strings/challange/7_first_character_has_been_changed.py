# Write a Python program to get a string from given string where all occurrences of its first character have been changed
# to '$', except the first character itself.

# Sample String: 'mama'
# Expected Result: 'ma$a'

my_str= 'unlucky' #'pineapple' #'success'
first_char = my_str[0]
result = my_str[1:].replace(first_char,'$')
print(first_char+result)

# Given solution
input_str = input('Enter a string: ')
char = input_str[0]
new_str = input_str[1:].replace(char,'$')
new_str=char + new_str
print(new_str)


# print(), len(), type(), sum(), max(), min(), round()- python built in methods

# str methods
# 'a'.str_method()
print(dir(str)) # shows all the methods available for str objects
help(str.replace) # shows the built-in method replace

s = 'Python'
new_s=s.upper() # converts all characters to uppercase
# non of these method will modify the original string
print(s) # original string remains unchanged
print(new_s) # new string with uppercase characters

print('pRogramminG'.lower()) # converts all characters to lowercase
s.capitalize() # converts the first character to uppercase and the rest to lowercase

# String Methods
my_str = 'I learn Python Programming.'

# 1. str.upper()
print(my_str.upper())

# 2. str.lower()
print(my_str.lower())

# 3. str.strip()- removes leading and trailing whitespace characters
ip = '  192.168.0.1    '
ip = ip.strip()
print(ip.strip())

value ='$$200$$$'
print(value.strip('$')) #

# 4. str.replace()
new_value = value.replace('$','€')
print(new_value)

# 5. str.count() - counts the occurrences of a substring in a string
txt = 'I learn PytHon, PythoN is cool!'
n = txt.count('Python')
print(n)
n2 = txt.lower().count('python')
print(n2)
print(txt.count('o'))

# 6. str.split()
my_list = txt.split()
print(my_list)

print('10.1.2.3'.split('.')) # dot symbol will be the seperator

# 7. str.join()
ip = '10.1.2.3'
ip_list = ip.split('.')
print(ip_list)

ip_str = 'xxxx'.join(ip_list)
print(ip_str)


# 8. str.find() - finds the first occurrence of a substring
my_str = 'I learn Python Programming.'
print(my_str.find('Python'))

# in
print('Python' in my_str) # checks if the substring is in the string

# not in
print('Golang' not in my_str) # checks if the substring is not in the string
# working with strings is to mix it with other data types and make a new string

first_name='Roman'
last_name = 'Pun'
age = 25
print('Hello ' + first_name + ' ' + last_name + '! You are ' + str(age) + ' years old.')

# Using f-strings for string formatting
# these f-strings are the string that have f in front of them
print(f'Hello {first_name} {last_name}! You are {age} years old.')

s = f'{2.3 *4.2/ 5.1:.4f}'  # This will format the result to 4 decimal places
print(s)  # This will print the result of the expression as string

# fahrenheit to celsius
# farenheit = celsius * 9/5 + 32
celsius = 15.
print(f'{celsius} degrees Celsius = {celsius * 9/5 + 32:.2f} degrees Fahrenheit.')

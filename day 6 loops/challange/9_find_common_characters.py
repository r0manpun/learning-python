# Write a Python program that finds the common characters that appear in two given strings.

str1 = input('Enter 1st string: ')
str2 = input('Enter 2nd string: ')

common_chars = ''
for char in str1:
    if char in str2:
        if char not in common_chars: # adding the common char only once
            common_chars += char

print(f'Common characters: {common_chars}')
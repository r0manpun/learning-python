# Write a Python program that counts and displays the vowels of a given string ignoring the letter case.

# Input str: Hello Everybody!
# Output: 5


# MY SOLUTION
# my_string = input('Enter a string: ').lower()
# vowels ='aeiou'
# total_vowels = 0
#
# for item in my_string:
#     if item in vowels:
#         total_vowels +=1
# print(total_vowels)


# SOLUTION
my_str = 'Cogito, expo sum.'
vowels ='aeiou'

count = 0
for v in vowels:
    if v in my_str.lower():
        count += my_str.count(v)

print(f'Total number of vowels: {count}')
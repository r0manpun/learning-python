# Given the string s1, write a program to return the sum and average of the digits that appear in the sting,
# ignoring all other characters.

# Input: Python31py50
# Output: Sum: 9, Average: 2.25

my_str = input('Enter a string with some digits in it: ')

total, count = 0, 0
for char in my_str:
    if char.isdigit():
        total += int(char)
        count +=1

print(f'Sum: {total}, Average: {total / count}')
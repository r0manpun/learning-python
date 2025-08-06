# Write a Python program that displays the multiplication table (form 1 to 10) of a specific integer number
# entered by user.

# Input : User enter 8

# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 8 x 10 = 80

print('It displays the multiplication table (form 1 to 10) of a specific integer number entered by user.')

my_input = int(input('Enter an integer number: '))

for i in range(1,11):
    print(f'{my_input} x {i} = {my_input * i}')
# Write a Python script that checks if a triangle is equilateral, isosceles or scalene.
# The user will be prompted for the triangle sides.

# Note:
# - An equilateral triangle is a triangle in which all three sides have the same length.
# - An isosceles triangle is a triangle that has two equal sides.
# - A scalene triangle is a triangle that has three unequal sides.

# Input: Enter the lengths of the triangle sides:
# x: 6
# y: 8
# z: 12

# Expected Output: Scalene triangle

x = int(input('Enter length of side x: '))
y = int(input('Enter length of side y: '))
z = int(input('Enter length of side z: '))

# MY SOLUTION
# if x == y == z:
#     print('Equilateral triangle')
# elif x == y or y == z or x == z:
#     print('Isosceles triangle')
# elif x !=y != z:
#     print('Scalene triangle')

# OTHER SOLUTION
if x + y <= z or y + z <= x or x + z <= y:
    print('Not a valid triangle')
elif x ==y ==z:
    print('Equilateral triangle')
elif x == y or y == z or x == z:
    print('Isosceles triangle')
else:
    print('Scalene triangle')


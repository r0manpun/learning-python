# Write a Python script that prompts the user for the radius of circle and calculates its area.
# Circle's area = pi * r **2 where pi= 3.1415
# Using an f-string display the area of the circle with 4 decimal places.

PI = 3.1415
radius = float(input('Enter the radius of circle: '))
area = PI * radius ** 2
print(f'Area of circle with a radius of {radius} is {area:.4f}')
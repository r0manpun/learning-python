# CONVERTING TYPES
from ctypes import c_float

# 1 miles = 1.60934 kilometers
# miles= float(input('Enter distance in miles: '))
# # print(type(miles))
# # miles = float(miles)
# km = miles * 1.60934
# print('Distance in km: ', km)

a = 10
b= 2.5
c = '8.2'

# int => float
a_float = float(a)
print('a: ', type(a))
print('a_float: ', type(a_float))

# float => int
b_int = int(b)
print('b_int: ', type(b_int))

# float => str
b_str = str(b)
print('b_str: ', type(b_str))

# str => float
c_float= float(c)
print('c_float: ', type(c_float))

# str => int
c_int = int(float(c))
print('c_int: ', type(c_int))

# str = 's'
# a= 1
# a_str = str(a)
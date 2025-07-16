# Floating point arithemetic: ISSUE and LIMITATIONS

# - Numbers in a computer are represented using bits (base 2), not decimal digits (base 10)
print(0.125 == 1/10 +2/100 + 5/1000)
# - Many decimal fractions cannot be represented exactly in binary and are only approximated by the
#   binary floating-point numbers stored in the machine
print((format(1/3,'.20f')))

print(format(1/10,'.20f'))
print(0.1,'.20f')
# - Some rational numbers cannot be represented using a finite number of digits
a = 0.1 * 3
b= 0.3
print(a==b) # False
print(format(a,'.25f'))

# Solving the Float problem. Writing Bugs-Free Code

# use isclose() module that is already defined in the python
from math import isclose
# isclose()
x = 0.0000001
y = 0.0000002
print(x==y)

print( isclose(x, y, abs_tol=0.01)) # abs_tol gives how much we want the decimal to compare

a = 9999999.01
b = 9999999.02
print(isclose(a, b, abs_tol=0.01))


a = 3.4
b= 2.3
print(a+b) # 5.7 !!!!
print(format(a,'.25f'))
print(format(b,'.25f'))

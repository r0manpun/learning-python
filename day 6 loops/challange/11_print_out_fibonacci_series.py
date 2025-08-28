# Write a Python script that prints out the Fibonacci series up to a given number n.
#
# Example:
# if n is 23 it will print out 0, 1, 1, 2, 3, 5, 8, 13, 21

my_input = int(input('Enter a number: '))

a, b = 0, 1
while a < my_input:
    print(a, '', end=' ')
    a, b = b, a + b


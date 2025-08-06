# Write a Python program to check if an integer (x) is the power of another integer (y).
# Prompt the user to input both integer.

# Input : 16, 2
# Output: 2 ** 4 = 16

x = int(input('Enter a number x: '))
y = int(input('Enter a number y to test if x which is (x) us a power of y: '))

found = False

for k in range (2, x//2):
    if y ** k ==x:
        print(f'{y} ** {k} == {x}')
        found = True
        break
else:
    print(f'{x} is not the power of {y}.')
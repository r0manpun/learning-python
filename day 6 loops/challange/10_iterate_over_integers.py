# Write a Python program that iterates over the integers from 1 to 50.
# For multiples of three print "Foo" instead of the number and for multiples of five print "Bar".
# For numbers that are multiples of both three and five print "FooBar".

for number in range(51):
    if number % 3 ==0 and number % 5 ==0:
        print('FooBar')
        continue
    elif number % 3 == 0:
        print('Foo')
        continue
    elif number % 5 == 0:
        print('Bar')
        continue
    print(number)

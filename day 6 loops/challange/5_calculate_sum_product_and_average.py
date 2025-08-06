# Write a program that calculates and displays the sum, the product and the average of n float numbers
# entered by the user, each on a separate line. Enter 0 to finish.


print('Enter some floats to calculate their sum, product and average. Input 0 to exit the input terminal.')

count = 0
total = 0.0
product = 1

while True:
    number = float(input(''))
    if number == 0:
        break

    total += number
    product *= number
    count +=1

if count < 2:
    print('Enter at least two number2s')
else:
    print(f'Sum: {total}')
    print(f'Product: {product}')
    print(f'Average: {total / count}')


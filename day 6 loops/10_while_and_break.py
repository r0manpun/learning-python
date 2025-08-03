# WHILE AND BREAK

# while True:
#     guest = int(input('Enter your lucky number [1-10]: '))
#     if guest == 7:
#         print('You won')
#         break
#     print(f'{guest} was not a lucky number!')


a = int(input('Enter number: '))
while a > 1:
    b = a // 2
    while b > 1:
        if a % b == 0:
            break
        b -= 1
    else: # belongs to inner while
        print(f'{a} is prime')
    a -= 1
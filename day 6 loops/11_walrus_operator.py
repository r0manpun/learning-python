# THE WALRUS OPERATOR
# - referred as column equals operator
# - allows us to both assign a value to a variable and to return that value all in the same expression.
# SYNTAX
# name := expression
# - expression is evaluated and then the result is assigned to the variable name.
# - the value assigned will also be returned.

# print(x := 2 + 2) # 4
# print(f'x is {x}') # x is 4

# value = input('Enter something: ')
# while value != '':
#     print(f'You entered: {value}')
#     value = input('Enter something: ')

# USING WALRUS OPERATOR
# while(value := input('Enter something: ')) != '':
#     print(f'You entered: {value}')


# data = input('Enter your name: ')
# if len(data) > 0:
#     print(f'Your name has {len(data)} characters.')
# else:
#     print(f'Your name cannot be empty.')

# USING WALRUS OPERATOR
data = input('Enter your name: ')
if (n := len(data))>0:
    print(f'Your name has {n} characters.')
else:
    print(f'Your name cannot be empty.')
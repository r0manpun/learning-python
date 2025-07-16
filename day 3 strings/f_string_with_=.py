# F-Strings with '=' for debugging

name , age = 'Roman', 25
print(f'Your name is {name} and your age is {age}.')
print(f'Your name is {name=} and your age is {age=}.')

r = 13.3
PI = 3.141592
print(f'Circle area with a radius of {r = } is {PI * r ** 2 = :.3f}')
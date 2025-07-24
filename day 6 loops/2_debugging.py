print('Hello Python!')
x= 101
y=x//2

for n in [1,2,3,4,5,6,7]:
    nn = n **2
    if nn % 2 ==0:
        print(f'{nn} is even.')
    else:
        print(f'{nn} is odd.')

# If we want to debug a program line by line:
# - The first step is to define where the program needs to be stopped.
#   And this is done using breakpoints. Breakpoints are spatial markers which represent places or conditions
#   when the debugger needs to step in a freeze the program state.
#   A program which has been frozen by the debugger is referred to as suspended.



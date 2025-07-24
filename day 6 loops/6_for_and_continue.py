# FOR, CONTINUE AND PASS STATEMENTS

for letter in 'Go Python goooo!':
    if letter=='o':
        continue
    print(letter,end='')

for n in range(10):
    if n % 2 == 0:
        print(f'Found an even number: {n}')
        continue
    print(f'Found an odd number: {n}')


# PASS STATEMENT - it is a null operation
# When it gets executed, nothing happens.
# Useful as a placeholder when a statement is required syntactically, but no code needs to be executed.

# Let's say I want to send 100 emails, but I haven't made up my mind about what libraries to use.
for _ in range(100):
    pass
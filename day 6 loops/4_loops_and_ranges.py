# LOOPS AND RANGES
# We use ranges in our program to execute repetitive task.

# Finding sum using loops and range
s = 0
for n in range(101):
    s +=n
print(f'Sum: {s}')

for _ in range(10):
    print('Do something', _)

# Example
# Let's assume we have a lottery application, and we want to pick three random winners.
# - In this case, we'll loop over range to repeat the process of choosing a random winner three times.

# "random" module - use to make or extract random value
import random
names =['Daniel','Diana', 'Paul','Ana', 'Dan','Victor','Marry','Alexander','Maria', 'Jeff','Bob','Bill','Angie']

for _ in range(3):
    print(f'Choosing winner: Round {_} ...')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)
    print('-----')


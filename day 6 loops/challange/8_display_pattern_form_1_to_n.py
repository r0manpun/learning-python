# Write a Python script that displays the following pattern from 1 to n where n is entered by user.

# If user enters 6 it will display:

# 1
# 22
# 333
# 4444
# 55555
# 666666



my_input = int(input('Enter an integer number: '))
for i in range(my_input + 1):
    print(str(i)* i)

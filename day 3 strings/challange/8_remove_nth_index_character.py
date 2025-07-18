# Write a Python program to remove the nth index character from a nonempty string.

def remove_nth_index(input_str, index):
        print( input_str[:index] + input_str[index+1:])


remove_nth_index('hello world',9)

# Given solution
n = int(input('Enter the nth index char to remove (number): '))
my_str = input('Enter the string to change: ')
first_part= my_str[0:n]
second_part= my_str[n+1:]
new_str = first_part + second_part
print(new_str)
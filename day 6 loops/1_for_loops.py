# FOR LOOPS

for letter in 'Python':
    # do something
    print(letter)
# Output
# P
# y
# t
# h
# o
# n

for number in {1,2,3}:
    print(number)
    print('bye')
print('#######')

# Print Vowels in string
my_str = input("Enter something: ")
vowels = 'aeiou'
for item in my_str:
    if item in vowels:
        print(item, end=' ')

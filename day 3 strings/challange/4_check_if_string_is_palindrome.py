# Write a Python script that tests if a string is a palindrome

def check_palindrome(input_str):
    if input_str[::-1]==input_str:
        return print(f'The string \'{input_str}\' is a palindrome')
    else:
        return print(f'The string \'{input_str}\' is not a palindrome')


check_palindrome('madam')
check_palindrome('roman')

s1 = 'mom'
print(f'Is {s1} palindrome? => {s1 ==s1[::-1]}')

s2 = 'eve'
print(f'Is {s2} palindrome? => {s2 ==s2[::-1]}')

s3 = 'daddy'
print(f'Is {s3} palindrome? => {s3==s3[::-1]}')
# Write a Python script that displays a number with a comma (,) as the thousands seperator (US and UK format)
# and with a period (.) as the thousands seperator (EU format)

# Sample input number: 1234567
# Expected Result: 1,234,567 and 1.234.567

# number = float(input('Enter the number to display: '))
n= 1234567
n_comma = f'{n:,}'
print(n_comma)
print(n_comma.replace(',','.'))
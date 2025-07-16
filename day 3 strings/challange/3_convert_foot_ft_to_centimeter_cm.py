# user will be prompted to enter the value in ft
foot = float(input("Enter the value in foot: "))
centimeter = foot * 30.48
print(foot ,'ft is equal to ', format(centimeter,'.2f'), 'centimeter' )
print(f'{foot} ft is equal to {centimeter:.2f} cm') # Using f-string for formatted output
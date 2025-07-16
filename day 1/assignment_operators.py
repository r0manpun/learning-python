# Equals (=)
a = 5

# Plus equals (+=) - increment assignment
a+=2 # shorthand for a = a + 2 => a is 7
print(a)

# Minus equals (-=) - decrement assignment
a-=3 # shorthand for a = a-3 => a is 4
print(a)

# Star equals (*=) - multiplication assignment
a*=2 # shorthand for a = a * 2 => a is 8
print(a)

# Slash equals (/=) - vision assignment
a /= 2  # a = a/2 => a is 4
print(a)

# Double stars equals (**=) - power assignment
a **= 2 # a= a ** 2 => a is 16
print(a)

# Percent equals (%=) - module assignment
# divmod()
a,b = divmod(14,6)
print(a,b) # Quotient - 2, Reminder- 2

# pow()
print(pow(5,9))

# sum()
print(sum([1,3,4,5,6,7]))

# max()
print(max([1,3,4,5,6,23,21]))

# min()
print(min([1,3,4,5,6,23,-21]))

# round() - does not change the variable but returns a new one with specified number of decimals
a = 5.646773
print(round(a,3)) # 3 - specified number of decimal
b = round(a,2)
print(a,b)
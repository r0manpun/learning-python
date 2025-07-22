# Boolean expression is a logical statement that is either True or False

# Logical (Boolean)  Operators:
# - and
# - or
# - not


# Boolean AND operator
# - It returns true if all expressions from the left hand side and from the right hand side of the operator returns true.
# - If any expression is false, the entire expression will be evaluated as false.
print('AND operator:')

age = 6
print((age>0 ) and (age <10)) # True

age = 20
print((age>0 ) and (age <10)) # False

# we can use multiple and operation
name = 'Daniel'
print((age>0 ) and (age <30) and (name== 'Daniel')) # True

print((age>0 ) and (age <30) and ('Danny' in name)) # False


# Boolean OR operator
# - at least one of the expression must be True for the compound expression to be considered True.
# - if all subexpression are False, then the entire compound expression is False.
print('OR operator:')

age , name = 6, 'Daniel'
print(age<3 or name == 'Andrei') # False
print(age<3 or name == 'Daniel') # True
print(age==6 or name == 'Andrei') # True
print(age!=6 or 'dan' in name) # False
print(age!=6 or 'dan' in name.lower()) # True

# Boolean NOT operator
# - converts True into False and False into True and vice versa.
print('NOT operator:')
print(not 2 == 2) # False
age =6
print(not age < 60) # True

name ='Daniel'
print(age<18 and not name == 'Andrei') # True - both 1st and 2nd case evaluate true so it is true. AND operator

print(not age == 6 or name =='Daniel') # True

print(not (age==6 or name =='Daniel')) # False

print(age<18 and name =='Daniel' or len(name)==6) # True


# Q. Why does logical operator AND and OR use something called short circuit evaluation or lazy evaluation?
#    What does it mean?
# - It means that Python evaluates the expression on the right only when it needs to.
#  Sometimes evaluating the first expression is enough to determine the final result.

a,b = 10,20
print(a>100 and b ==20) # False
# with AND operator having any test condition evaluated to fals makes the entire expression false as well.
# it would be a waste of resource to evaluate the remaining expression.

print(a == 100 or b < 0) # False
# In contrast, OR operator evaluates the operand on the right only if the first operand is false.
# If it's true, then the whole expression is true and it doesn't depend on the second test condition.
print(a == 10 or b < 0) # True

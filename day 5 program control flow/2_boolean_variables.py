# Boolean variable is an object of the bool class which is an int subclass

# Boolean Constants:
# 1. True
# 2. False


print(issubclass(bool, int)) # True
print(int(True)) # 1
print(int(False)) # 0

print(id(True)) # 4393956584
print(id(4>2)) # 4393956584
# id of 'True' is always the same as id of any true condition
print((4 > 2) == True) # True
print((4 > 2) is True) # True

# The value of true is one, and the value of false is zero, but true and one respectively.
# False and zero are not the same object or are not saved at the same memory address.
print(True == 1 ) # True
print(True is 1) # False - address on One is not equal to the address of True
print(id(1)) # 4393970104, while the address of True is 4393956584

print(3==False) # False
print('4' == 4) # False

# boolean are integers
print(True > False) # True

# TRUTHNESS OF OBJECTS

result = ''
if bool(result):
    print('result is not empty.')
else:
    print('result is empty.')

var1 = ''
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')
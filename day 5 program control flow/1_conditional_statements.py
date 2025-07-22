# if some_condition_is_true:
 # 1. execute_this_code
# elif some_other_condition_is_true:
 # 2. execute_this_code
# else:
 # 3. execute_this_code
# fi

# Q.1 let's suppose we have a some sort of booking application for airline tickets, and the application
# checks the balance of a bank account and only if the value is greater or equal to the price
# of the flight ticket, it will continue the booking process. reserve the seat and so on

# balance = 100
# price = 50
#
# if balance >= price:
#     new_balance = balance - price
#     print(f'You can book the flight and your new balance will be {new_balance}.')
# else:
#     print(f'Insufficient balance! Please deposit {price-balance}.')
#
#
# print('Other instructions...')
# x= 10

# Note: in Python we use colons ":" and indentations instead of curly brackets "{}" to define block of code


# NESTED IF ElIF ELSE STATEMENT

# answer = input('Do you wanna continue? Enter yes or no: ').lower()
# # answer = answer.lower()
# if answer == 'yes':
#     print('We\'ll move on.')
# elif answer == 'no':
#     print('We\'ll stop.')
# else:
#     print('Invalid answer.')

# Q.2 let's suppose we have a some sort of booking application for airline tickets, and the application
# checks the balance of a bank account and only if the value is greater or equal to the price
# of the flight ticket, it will continue the booking process. reserve the seat and so on.Add: We continue if the
# user accept it to continue

# balance = 100
# price = 50
#
# if balance >= price:
#     new_balance = balance - price
#     print(f'You can book the flight and your new balance will be {new_balance}.')
#     answer = input('Do you wanna continue? Enter yes or no: ').lower()
#     if answer == 'yes':
#         print('We\'ll continue.')
#     elif answer == 'no':
#         print('We\'ll stop.')
#     else:
#         print('Invalid answer.')
# else:
#     print(f'Insufficient balance! Please deposit {price - balance}.')


x = 10
if x <=10:
    print("x is less than or equal to 10.")
elif x == 10:
    print("x is equal to 10.")
else:
    print("x is not equal to 10.")

# Note: It will only return the first block of code
# Output will be: 'x is less than or equal to 10.'
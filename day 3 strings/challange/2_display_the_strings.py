# It displayed: "You've got an error!"
# \n means a new line.
# \ is known as the escape character.

print('It displayed: "You\'ve got and error!" \n\\n means a new line. \n\\ is known as the escape character.' )

# Other solutions
message = "It displayed: \"You\'ve got an error!\""

message_2 = 'It displayed: "You\'ve got an error!"'
print(message)

print('\\n means a new line.')
print(r'\n means a new line.') # r before the string means raw string, it will not interpret escape characters
print('\\ is known as the escape character.')
print(r'\ is known as the escape character.')

# a string is an ordered sequence of UTF-8 encoded characters

my_str1= 'I am learning Python.'
my_str2= "I am learning Python."

print(my_str1)

# Hi there! I'm Roman.
print('Hi there! I\'m Roman')
print("Hi there! I'm Roman")

message = 'He said: "Go for it!"'
print(type(message))

languages = """
I like python
Javascript 
and 
C#.
""" # """ """ are called multi line strings
# this is also use to create doc strings
print(languages)

my_languages = 'I like Python\nJavascript\nand\nC#.'
print(my_languages)
# \ - escape character
# \t - tab
# \n - new line
print('a\tb\tc\td\ne')
print('\\n') # returns \n
print('He says: "I\'m 24"')
print('\\ is a special character in Python.')

print('こんにちは世界')  # This prints "Hello World" in Japanese

hi = '🙂'
print(hi)
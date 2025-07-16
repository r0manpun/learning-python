# + => the concatenation operator

movie = 'The Godfather'
director = 'Francis Ford Coppola'
movie_and_director = movie + director
print(movie_and_director)
print( movie + ' was directed by ' + director)

print('abc' '123') # abc123
lang = 'Python'
version= 3.10
print(lang + str(version))


# * => the repetition operator
print(movie * 5) # prints the movie 5 times
print('#' * 50) # prints the # 50 times
price = '10.5'
print(price * 3) # prints the price 3 times, but as a string, to multiply a number we need to convert it first
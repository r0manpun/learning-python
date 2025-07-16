movie = 'The Godfather'
print(movie[0:2]) # it will print substring from index 0 to 2 (not including 2)

# string_variable[start:end] => slicing
print(movie[2:5])
print(movie[:2]) # it will print substring from index 0 to 2
print(movie[4:]) # it will print substring from index 4 to the end
print(movie[-2:]) # it will print substring from index -2 to the end

# movie[:1] + movie[1:] is equal to movie
print(movie[:4] + movie[4:])
print(movie[:42]) # it will print substring from index 0 to 42, but since the string is shorter, it will print the whole string
# The Godfather
print(movie[3:100]) # it will print substring from index 3 to the end, even if the end index is larger than the length of the string
#  Godfather
print(movie[0:10:2]) # it will print substring from index 0 to 10 with step 2, so it will print every second character
# TeGda
print(movie[::]) # it will print the whole string
# The Godfather
print(movie[::-1]) # it will print the whole string in reverse order
# rehtafdoG ehT
print(movie[::-2]) # it will print the whole string in reverse order with step 2, so it will print every second character in reverse order
# rhadGeT
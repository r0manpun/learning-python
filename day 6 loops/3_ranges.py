# RANGES

r = range(2,10)
print(type(r))
print(r) # range(2,10)
print(list(r)) # [2, 3, 4, 5, 6, 7, 8, 9]

# range(start,end,step)
# start- starts the range from
# stop - stops the range at
# step - how big the gap is on each range. Like suppose step is 2, if range starts from 2 and stops at 10 then the result will be
#        [2, 4, 6, 8]

# Generating list of all even numbers from 0 to 10
print(list(range(0,11,2))) # [0, 2, 4, 6, 8, 10]

# divisible by 7 from 0 to 40
print(list(range(0,40,7))) # [0, 7, 14, 21, 28, 35]

# sum of all number from 0 to 1_000
s = sum(range(0,1_001))
print(s) # 500500

# In summery we can all range in three different ways
# 1. with one argument
# range(stop) - generates the sequence of numbers from zero included to that argument excluded in steps of one.
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# This is the same as range(0,10,1) or range(0,10)

# 2. With two argument
# range(start,stop)
print(list(range(3,9))) # range(3,9,1)

# 3. With three argument
print(list(range(5,100,13))) # [5, 18, 31, 44, 57, 70, 83, 96]
print(list(range(-20,10,4))) # [-20, -16, -12, -8, -4, 0, 4, 8]

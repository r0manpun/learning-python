# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each
# number less than the asked number.

# number
# list of divisors of each number

# for num in number
# let d = num - 1
# if num % d == 0
# print(d)

# MY PROBLEM TRY
# num = int(input('Enter a number: '))
# print(list(range(1,num)))
# for a in list(range(1,num)):
#    b = num - 1
#    if a % b == 0:
#        print(b)
#    a +=1

# SOLUTION
num = int(input('Enter a number: '))
all_divisors = list()
for i in range(2, num//2+1):
    if num % i == 0:
        all_divisors.append(i)
print(all_divisors)

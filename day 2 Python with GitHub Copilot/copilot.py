# function that returns prime numbers in a given range
def prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

prime_list = prime_numbers(1,100)
print(prime_list)

# funtion that returns the
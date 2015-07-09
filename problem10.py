#!/usr/bin/env python3

from math import sqrt


def is_prime(num):
    """
        primes needs to contain all primes lower than num
        how to start it? not sure
    """
    test_limit = sqrt(num) + 1   # The highest we ever need to calculate
    for i in primes:
        if i > test_limit:
            break
#        print("Dividing {0} by {1}".format(num, i))
        if num % i == 0:
            return False

    return True


primes = [2]

total = 1
for i in range(3, 2000001, 2):
    print("Testing {0}".format(i))
    if is_prime(i):
        primes.append(i)
        total += i

print(total)

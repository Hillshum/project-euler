#!/usr/bin/env python3
###########################################3
# For ProjectEuler.net #37
# Truncatable primes
#
#
#
#
###################################################

from math import log10

def is_prime(num, cache=None):

    if not cache:
        tests = range(3, int(num**.5) + 1, 2) 
    else:
        tests = cache
    
    if num is 1:
        return False
    if num is 2:
        return True
    
    if num % 2 is 0:
        return False

    for i in tests:
        #print("i is {0}, num is {1}".format(i, num))
        if i > num**.5:
            return True
        if num % i == 0:
            return False
    return True


def primes(limit=None):

    if not limit:
        limit = 200000

    yield 2
    yield 3

    cache = [3]

    for i in range(5, limit, 2):
        if is_prime(i, cache):
            cache.append(i)
            yield i
    
    raise StopIteration
    
BASE_PRIMES = [2, 3, 5, 7]

def truncatable_left(num):
    test = num % 10**int(log10(num))

    if not is_prime(test):
        return False

    if test > 9:
        return truncatable_left(test)
    else:
        return True

def truncatable_right(num):
    test = num // 10
    if not is_prime(test):
        return False

    if test > 9:
        return truncatable_right(test)
    else:
        return True



if __name__ == '__main__':
    truncatables = []
    for prime in primes(5000000):
        if truncatable_right(prime) and truncatable_left(prime):
            truncatables.append(prime)

    print(sum(truncatables))

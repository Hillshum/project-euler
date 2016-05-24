#!/usr/bin/env python3
###########################################3
# For ProjectEuler.net #37
# Truncatable primes
#
#
#
#
###################################################

def is_prime(num, cache=None):

    if not cache:
        tests = range(3, int(num**.5) + 1, 2) 
    else:
        tests = cache

    for i in tests:
        #print("i is {0}, num is {1}".format(i, num))
        if i > num**.5:
            return True
        if num % i == 0:
            return False
    return True

def primes(limit=None):

    if not limit:
        limit = 500000

    yield 2
    yield 3

    cache = [3]

    for i in range(5, limit, 2):
        if is_prime(i, cache):
            cache.append(i)
            yield i
    
    raise StopIteration
    
POSSIBLE_RIGHTS = [1,3,7,9]

def expand_right(num):
    possibles = []
    finished = True

    for i in POSSIBLE_RIGHTS:
        test = num * 10 + i
        if is_prime(test):
            possibles.append(test)
            finished = False
    print(possibles)
    for i in possibles:
        expand_right(i)

def expand_left(num):
    possibles = []
    finished = True

    for i in range(1, 11):
        test = num + 10 * i
        if is_prime(test):
            possibles.append(test)
            finished = False
    
    print(possibles)
    for i in possibles:
        expand_left(i)

if __name__ == '__main__':
    expand_left(37)

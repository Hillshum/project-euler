#!/usr/bin/env python3
#

# This program calculates the nth prime. In particular we are looking for the
# 10,001th prime
#
# It should not take more than maybe 15 minutes tops, preferably less, on
# a standard desktop computer
#

def is_prime(num):
    for i in range(2,round(num/2)+2):
        if num % i == 0:
            return False

    return True


def list_primes(start=3, end=10001):
    n = start
    primes = [1,2]
    while len(primes)<end:
        if is_prime(n):
             print('{0} is prime'.format(n))
             primes.append(n)

        n += 1
    return primes
    

#!/usr/bin/env python3

# This is for problem 12 at projecteuler.net

from math import floor, sqrt


def iter_triagnles(stop, start=1):
    t = start
    for i in range(start + 1, stop):
        yield t
        t += i


class Primes(object):
    """Stores a collection of prime numbers and associated multiplicites"""

    def __init__(self, prime_list=None):
        self.primes = {}
        if prime_list:
            self.append(prime_list)

    def append(self, prime_list):
        # TODO: Make it detect a single tuple
        for p, m in prime_list:
            if self.primes.get(p):
                self.primes[p] += m
            else:
                self.primes[p] = m

    def get(self, prime, default=None):
        try:
            return self[prime]
        except ValueError:
            return default

    def items(self):
        return self.primes.items()

    def __str__(self):
        r = ["{0}**{1} * ".format(p, m) for p, m, in self.primes.items()]
        return ''.join(r)

    def __repr__(self):
        return str(list(self.primes.items()))

    def __getitem__(self, key):
        return self.primes[key]

    def __setitem__(self, key, value):
        self.primes[key] = value

    def __delitem__(self, key):
        del self.primes[key]

    def __add__(self, other):
        if isinstance(other, Primes):
            r = self.primes.copy()

            for p, m in other.primes.items():
                if p in r:
                    r[p] += m
                else:
                    r[p] = m
            return r
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(self, other)

    def __iadd__(self, other):
        self.append(other)
        return self

    def __iter__(self):
        return iter(self.primes.items())

    def __len__(self):
        l = 0
        for p, m in self.primes.items():
            l += m
        return l


class FactorCounter(object):

    def __init__(self, CACHE=True):
        self.CACHE = CACHE
        if self.CACHE:
            self.cache = {}

    def factor_triangles(self, stop=100000000000):
        for triangle in iter_triagnles(stop):
            primes = self.get_primes(triangle)
            count = self.get_factors_from_primes(primes)
            print("{0} has {1} factors".format(triangle, count))
            if count > 500:
                return triangle

    def get_factors_from_primes(self, primes):
        count = 1
        for p, m in primes:
            count *= m + 1
        return count

    def get_primes(self, num):
        if self.cache.get(num):
            return self.cache[num]

        if num in (1, 2, 3):
            return Primes([(num, 1)])
        r = floor(sqrt(num))

        for i in range(2, r + 1):
            if num % i == 0:
                primes = Primes(
                    [(p, m) for p, m in self.get_primes(int(num / i))])
                primes.append([(i, 1)])
                return primes

        return Primes([(num, 1)])

    def _count_factors(self, num):
        count = 2  # Num and 1 are always factors

        for i in range(2, 1 + floor(sqrt(num)), 1):
            print('Checking {0}'.format(i))
            if num % i == 0:

                if self.CACHE and self.cache.get(i):
                    count += self._process_cache_hit(num, i)
                    print('Count is {0}'.format(count))

                else:
                    dividend = int(num / i)

                    if dividend == i:  # Don't double count sqrts
                        count += 1
                    else:
                        count += 2
                    print('Count is {0}'.format(count))

        if self.CACHE:
            self.cache[num] = count
        return count

    def _process_cache_hit(self, num, i):
        print('Found {0} in cache'.format(i))
        add = self.cache[i]   # Minus for num and i
        print('Adding {0}'.format(add))
        return add

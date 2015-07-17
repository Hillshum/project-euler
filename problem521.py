#!/usr/bin/env python3


class Problem521Solver:

    def __init__(self, limit=1000000000000, build_cache=True):
        if build_cache:
            self.primes = [1, 2, 3]
            self.cache_primes(limit)

    def _is_prime(self, num):
        """
        Only usable for finding primes in sequence
        """
        if num in {1, 2, 3}:
            return True

        for i in self.primes[2:]:
            # print("Checking {} against {}".format(num, i))
            if num % i == 0:
                return False

        return True

    def cache_primes(self, limit):
        self.primes = [1, 2, 3]
        for i in range(5, int(limit / 2) + 1, 2):
            if self._is_prime(i):
                self.primes.append(i)

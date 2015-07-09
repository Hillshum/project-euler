#!/usr/bin/env python3

# ##################################################################
#
#
#
# projecteuler.net problem 21
#
#
#
#
#
#
#
#
#
#
# #####################################################################3


class Problem21Solver(object):

    def get_divisors(self, num):
        divisors = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(int(num/i))
        divisors.sort()
        return divisors[:-1]

    def get_all_divisors(self, limit=10000):
        divisors = {i: self.get_divisors(i) for i in range(1, limit + 1)}
        return divisors

    def sum_all_divisors(self, divisors):
        return {k: sum(v) for k, v in divisors.items()}

    def find_amicable_numbers(self, sums):
        amicables = []
        for num, sum_ in sums.items():
            if sum_ < 10000 and num != sum_ and sums[sum_] == num:
                amicables.append(num)

        return amicables

    def solve(self):
        return sum(
            self.find_amicable_numbers(
                self.sum_all_divisors(
                    self.get_all_divisors()
                )
            )
        )

if __name__ == '__main__':
    print(Problem21Solver().solve())

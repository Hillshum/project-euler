#!/usr/bin/env python3

#########################################################

# Given a pyramid of numbers, find the largest possible route
# from top to bottom

############################################################


FILEPATH = 'problem18.txt'


class Pyramid:

    def __init__(self, filepath=FILEPATH):
        self.counted = False
        self.parse_file(filepath)

    def __str__(self):
        return ''.join(['{}\n'.format(row) for row in self._store])

    def parse_file(self, path=FILEPATH):
        f = open(path)
        self._store = [[int(num) for num in line.split()]
                       for line in f.readlines()]

    def _add_below(self, r_index, col_index):
        # print('Adding [{}][{}]'.format(r_index, col_index))
        left_child = self._store[r_index + 1][col_index]
        right_child = self._store[r_index + 1][col_index + 1]
        larger_child = left_child if left_child >= right_child else right_child
        return self._store[r_index][col_index] + larger_child

    def compute_totals(self):

        # We need to iterate over the array backwards, preserving the
        # indexes for use elsewhere. Also, we don't process the last one
        # This may not be very pythonic as we have to lookup the row...
        # The alternative is to determine the 'forward' index based on the
        # 'reversed' one..something like forward = len - reversed
        for r_index in range(len(self._store) - 2, 0, -1):

            row = self._store[r_index]
            # print(row)
            self._store[r_index] = [self._add_below(
                r_index, i) for i, num in enumerate(row)]

        self.counted = True

    def solve(self):
        self.counted or self.compute_totals()

        first = self._store[0][0]

        left_child = self._store[1][0]
        right_child = self._store[1][1]

        return first + (left_child if left_child > right_child else right_child)

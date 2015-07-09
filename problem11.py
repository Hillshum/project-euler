#!/usr/bin/env python3

# This is for Problem 11 at projecteuler.net


class Grid(object):

    def __init__(self, filename):
        f = open(filename)
        self.lines = []
        for line in f.readlines():
            self.lines.append(line.strip().split(' '))
        self.lines = [[int(col) for col in line] for line in self.lines]
        print(self)

    def __str__(self):
        s = []
        for line in self.lines:
            for col in line:
                s.append("{0} ".format(col, width=2))  # Needs width-alignment
            s.append('\n')
        return ''.join(s)

    def __getitem__(self, key):
        return self.lines[key]

    def iter_linear(self):
        for line in self.lines:
            for col in line:
                yield col

    def count_right(self, row, col):
        try:
            return self[row][col] * self[row][col + 1] * self[row][col + 2] * \
                self[row][col + 3]
        except IndexError:
            return None

    def count_down(self, row, col):
        try:
            return self[row][col] * self[row + 1][col] * self[row + 2][col] * \
                self[row + 3][col]
        except IndexError:
            return None

    def count_down_right(self, row, col):
        self[row][col]
        try:
            return self[row][col] * self[row + 1][col + 1] \
                * self[row + 2][col + 2] * self[row + 3][col + 3]
        except IndexError:
            return None

    def count_down_left(self, row, col):
        try:
            return self[row][col] * self[row + 1][col - 1] \
                * self[row + 2][col - 2] * self[row + 3][col - 3]
        except IndexError:
            return None

    def count_following(self, row, col):
        counts = (self.count_right(row, col),
                  self.count_down(row, col),
                  self.count_down_left(row, col),
                  self.count_down_right(row, col))
        return counts

    def count_all(self):
        counts = []
        for irow, row in enumerate(self):
            for icol, col in enumerate(row):
                counts.append(self.count_following(irow, icol))
        return counts

    def get_greatest_count(self):
        greatest = 0
        counts = self.count_all()
        for square in counts:
            for direction in square:
                if direction and direction > greatest:
                    greatest = direction
        return greatest

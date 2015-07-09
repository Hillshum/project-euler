#!/usr/bin/env python3

###############################################################
# This is for projecteuler.net Problem 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes exist for a 20x20 grid?
#
# Note that while the problem described the journey as upper-left to
# bottom-right, this code makes the most sense if the grid is imagined on the
# Cartesian plane with the desination as the center (0,0) and the start as a
# point to the upper-right.
#
###########################################################################

import sys


class PathCache(dict):
    def __getitem__(self, key):
        x, y = key

        if not (x and y):  # If one of them is zero
            return 1
        if x < y:
            key = y, x
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        x, y = key
        if x < y:
            key = y, x
        return dict.__setitem__(self, key, value)

    def __init__(self):
        self[1, 1] = 2


class PathCounter(object):

    def __init__(self, x=20, y=20):
        self.x = x
        self.y = y
        self.cache = PathCache()

    def count_paths(self, x, y, level=0):
        """
        Start at the desination, and calcuate every option from there.

        We basically march up the grid one row at a time, using a combinatorial
        algorithm.

        This takes a couple shortcuts. We know that the number of paths for any
        x,y position is equal to the number of paths for y,x, so we rely on our
        cache object to convert between them.

        """
        path_count = 2

        for iy in range(1, y + 1):
            for ix in range(2, x + 1):
                path_count = self.cache[ix - 1, iy]
                # print("iteration with {0},{1} and last count {2}".format(
                #    ix, iy, path_count))
                # print('Adding {0} to path_count'.format(num_to_add))
                path_count += self.cache[ix, iy - 1]
                self.cache[ix, iy] = path_count
                # print("Adding {0},{1}:{2} to cache".format(
                #    ix, iy, path_count))

        return path_count


if __name__ == "__main__":
    pc = PathCounter()

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(pc.count_paths(x, y))

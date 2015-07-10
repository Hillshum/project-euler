#!/usr/bin/env python3

# ########################################################################3

# Problem 67 is the same as #18 but with a larger dataset (that can't be
# brute-forced). I wrote an efficient algorith for #18 however, so I just
# use that here

# ########################################################################

from problem18 import Pyramid

if __name__ == '__main__':

    a = Pyramid('problem67.txt')
    print(a.solve())

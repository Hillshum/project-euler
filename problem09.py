#!/usr/bin/env python3
################################################################
# This program looks for the pythagorean triplet where a + b + c == 1000
# Only one should exist
##################################################################

from math import sqrt


class PythagoreanTriplet():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c

    def product(self):
        return self.a * self.b * self.c


class PythagoreanTripletFinder():
    def __init__(self):
        self.squares = [i**2 for i in range(0, 20000)]
        self.primitive_squares = []
        self.primitive_hypos = []

    def is_primitive(self, triplet):
        """
        Note that this method requires that the primitive_hypos array contains
        all primitive hypos < triplet[2]
        """
        hypo = triplet[2]
        for i in self.primitive_hypos:
            if hypo % i == 0:
                return False
        return True

    def find_triplets(self, c, only_primitives=True):
        """
        Given c, use the sequence of odd numbers to evaluate each
        perfect square < c**2 by subtracting it from c and then
        checking if a perfect square.


        """

        print("Checking {0} for triplets".format(c))
        triplets = []

        c_squared = b_squared = c**2

        for i in range(c * 2 - 1, 1, -2):
            b_squared -= i
            a_squared = c_squared - b_squared
            if a_squared > b_squared:
                break
            # triplet_squared = a_squared, b_squared, c_squared
            if a_squared in self.squares:  # If it is a valid triplet
                triplet = (int(sqrt(a_squared)), int(sqrt(b_squared)),
                           int(sqrt(c_squared)))
                if only_primitives:
                    if not self.is_primitive(triplet):
                        break
                triplets.append(triplet)
        return triplets

if __name__ == "__main__":
    finder = PythagoreanTripletFinder()
    triplets = []
    for i in range(1, 1000):
        for triplet in finder.find_triplets(i):
            triplets.append(triplet)
    print (triplets)
    for triplet in triplets:
        triplet_sum = triplet[0] + triplet[1] + triplet[2]
        if triplet_sum == 1000:
                print(triplet)

#!/usr/bin/python

# This is for Project Euler #14 at projecteuler.net

def collatz(n):
    """ The Collatz Conjecture states that after some number of steps, a result
    of 1 will be found for any n. See below for definition of the sequence.
    
    This function counts the steps taken to reach 1
    """
    steps = 0 
    while n > 1:

        if n % 2 == 0:
            n = n/2
            steps +=1

        else:
            n = (n*3 + 1)/2
            steps +=2

    return steps


def try_numbers(max=1000000):
    """ This function keeps track of the number of steps taken for a large 
    set of numbers.
    """
    
    highest = (1,0) # a 2-tuple to keep track of the higest
    counts = {} # Dict for caching
    for i in range(2,max):
        steps = collatz(i)
        if steps > highest[1]:
            highest = i, steps


    return highest


def cached(max=1000000):
    """ This function uses caching to perform the functionality of try_numbers()
    far more efficiently. It does not use collatz() because the caching bits go
    in both of the above functions.
    """

    highest = (1,0) # Keep track of the highest
    counts = {} # The cache

    for i in range(2,max):
        
        n = i # Make a separate variable for this subroutine
            
        steps = 0 
        while n > 1:

# Search the cache
            if n in counts:
                steps += counts[n]
                break

            if n % 2 == 0:
                n = n/2
                steps += 1

            else:
                n = (n*3 + 1)/2
# No two odd numbers may appear consecutively. This skips a bit of logic.
                steps += 2 # Remember that such a skip counts as two steps.

        counts[i] = steps
        if steps > highest[1]:
            highest = i, steps

    return highest


def uncached(max=1000000):
    """ This is an exact duplicate of chached() but without the caching
    bit. Exists for purpose of comparing the two.
    """

    highest = (1,0) # Keep track of the highest

    for i in range(2,max):
        
        n = i # Make a separate variable for this subroutine
            
        steps = 0 
        while n > 1:

            if n % 2 == 0:
                n = n/2
                steps += 1

            else:
                n = (n*3 + 1)/2
# No two odd numbers may appear consecutively. This skips a bit of logic.
                steps += 2 # Remember that such a skip counts as two steps.

        if steps > highest[1]:
            highest = i, steps

    return highest

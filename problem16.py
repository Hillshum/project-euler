#!/usr/bin/python

# This is frr Project Euler #16 at projecteuler.net

num = 2**1000

def add_digits(num):
    
    num = str(num) # Convert the number to an iterable string. 
# A list might work better, but I'm to lazy to figure out how to convert to such

    total = 0 # Add each digit to this total

    for i in num:
        
        total += int(i)

    return total

#if __name__ == __main__ :
#    print add_digits(num)

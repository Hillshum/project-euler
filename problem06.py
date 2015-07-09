#!/usr/bin/python

# This is for Project Euler #8, at projecteuler.net


def get_max(num):
    

    max = 0
    num = str(num)
    
    for i in num:
        
        e = int(i)

        a = int(num[e]) * int(num[e+1]) * int(num[e+2]) * int(num[e+3]) * int(num[e+4])

        if a > max:
            max = a

    return max

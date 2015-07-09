#!/usr/bin/python

# This is for Project Euler #8, at projecteuler.net


def get_max(num):
    

    max = 0
    num = str(num)
    
    for i in range(len(num)-4):
        

        a = int(num[i]) * int(num[i+1]) * int(num[i+2]) * int(num[i+3]) * int(num[i+4])

        if a > max:
            max = a

    return max

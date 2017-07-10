#!/usr/bin/env python3

from math import log, floor

fib_len = 0
index = 2
a = 1
b = 1

while fib_len < 999:
    c = a + b
    a = b
    b = c

    print(c)
    fib_len = floor(log(b, 10))
    index += 1


print(index)



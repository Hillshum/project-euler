#!/usr/bin/env python3


def solve():
    i = 20
    while True:
        for a in [19,18,17,16,15,14,13,12,11,]:
            print("Testing {0} against {1}".format(i,a))
            if i%a != 0:
                break
        else:
            print("Success! {0}".format( i))
            return
        i += 10


def solve_10():
    i = 10
    while True:
        for a in [9,8,7,6,5]:
            print("Testing {0} against {1}".format(i,a))
            if i%a != 0:
                break
        else:
            print("Success! {0}".format( i))
            return
        i += 10


def test_divisibility(num):
    for i in range(20,10,-1):
        if num % i == 0:
            continue
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    solve()

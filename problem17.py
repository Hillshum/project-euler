#!/usr/bin/env python3

# #####################################################################3
#
#
#
#
# This is for projecteuler.net #17
#
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
# and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.
#
#
#
# This code doesn't fully solve the problem, but the rest is pretty
# straightforward
#
###########################################################################


def convert_one_digit(num):
    if num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'
    else:
        raise TypeError(str(num) + ' is not valid here.')


def convert_two_digit(num):
    """This is the smallest block that can stand on its own."""
    if num >= 100:
        raise TypeError(str(num) + ' is not valid here.')

    def convert_teen(num):

        def convert_high_teen(num):
            if not 16 <= num <= 19:
                raise TypeError(str(num) + ' is not valid here.')

            elif num == 16:
                return 'sixteen'
            elif num == 17:
                return 'seventeen'
            elif num == 18:
                return 'eighteen'
            elif num == 19:
                return 'nineteen'

        if num < 10:
            return convert_one_digit(num)
        elif num == 10:
            return 'ten'
        elif num == 11:
            return 'eleven'
        elif num == 12:
            return 'twelve'
        elif num == 13:
            return 'thirteen'
        elif num == 14:
            return 'fourteen'
        elif num == 15:
            return 'fifteen'
        elif num == 16:
            return 'sixteen'
        elif num == 17:
            return 'seventeen'
        elif num == 18:
            return 'eighteen'
        elif num == 19:
            return 'nineteen'
        else:
            raise TypeError(str(num) + ' is not valid here.')

    def convert_tens_place(num):
        if num == 1:  # things like 'eleven' need special attention
            raise TypeError(str(num) + ' is not valid here.')
        elif num == 2:
            return 'twenty'
        elif num == 3:
            return 'thirty'
        elif num == 4:
            return 'forty'
        elif num == 5:
            return 'fifty'
        elif num == 6:
            return 'sixty'
        elif num == 7:
            return 'seventy'
        elif num == 8:
            return 'eighty'
        elif num == 9:
            return 'ninety'
        else:
            raise TypeError(str(num) + ' is not valid here.')

    if num < 20:
        return convert_teen(num)
    elif num >= 20:
        ones = num % 10
        suffix = '-' + convert_one_digit(ones) if ones else ''
        return convert_tens_place(num//10) + suffix
    else:
        raise TypeError(str(num) + ' is not valid here.')


def convert_number(num):
    if type(num) != int:
        raise TypeError(str(num) + ' is not valid here.')

    if num > 1000:
        raise NotImplementedError("No support for " + str(num))

    if num == 1000:
        return 'one thousand'
    elif num >= 100:
        last = num % 100
        suffix = ' and ' + convert_two_digit(last) if last else ''
        return convert_one_digit(num//100) + ' hundred' + suffix
    elif num >= 10:
        return convert_two_digit(num)
    elif num > 0:
        return convert_one_digit(num)
    else:
        raise NotImplementedError("No support for " + str(num))

# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    numList = []
    for i in xrange(start, stop, step):
        numList.append(i)
    return numList
    pass


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    loneRanger = []
    index = start
    while (index < stop):
        loneRanger.append(index)
        index = index + step
    return loneRanger
    pass


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    twoStepRanger = []
    for i in xrange(start, stop, 2):
        twoStepRanger.append(i)
    return twoStepRanger
    pass


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    index = start
    evenOddRange = []
    evenOdd = 0
    while (index < stop):
        evenOddRange.append(index)
        if evenOdd % 2 == 1:
            index = index + odd_step
        else:
            index = index + even_step
        evenOdd = evenOdd + 1
    return evenOddRange
    pass


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    message = "Enter a Numer between {low} and {high}: ".format(low=low,
                                                                high=high)
    number = int(raw_input(message))
    while True:
        if (low < number < high):
            print("{} is fine.".format(number))
            return number
        else:
            number = int(raw_input("Please enter another number: "))
    return number
    pass


def not_number_rejector():
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "Enter a number: "
    while True:
        try:
            number = int(raw_input(message))
        except ValueError:
            print("You did not enter a number!")
            continue
        else:
            print("{} is fine.".format(number))
            return number


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = "Enter a Numer between {low} and {high}: ".format(low=low,
                                                                high=high)
    while True:
        try:
            number = int(raw_input(message))
        except ValueError:
            print("You did not enter a number!")
            continue
        else:
            if (low <= number <= high):
                print("{} is fine.".format(number))
                return number
            else:
                print("This number is not between " + str(low) + " and "
                      + str(high))
    pass


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector()
    print("\nsuper_asker")
    super_asker(33, 42)

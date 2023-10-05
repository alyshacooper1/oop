import random

# The Coin class simulates a coin that can
# be flipped.

class Coin: # Class definition
    # The _ _init_ _ method initializes the (how to create obj)
    # sideup data attribute with 'Heads'.
    # first parameter is always self

    def __init__(self):
        self.__sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.__sideup

# set method - mutated to change attribute in
# get method - used for repairing an attribute
# don't run this program bc it's just a blueprint
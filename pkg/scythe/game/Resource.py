# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


class Resource(tuple):
    """
    The base class for game resources
    """


    # arithmetic; there are no in-place versions since tuples are read-only
    # combine two instance to make a new one
    def __add__(self, other):
        # go through my resources and {other}'s and add them together
        return type(self)(r1+r2 for r1, r2 in zip(self, other))

    def __sub__(self, other):
        # subtract {other}'s resources from mine
        return type(self)(r1-r2 for r1, r2 in zip(self, other))

    # scalar multiplication
    def __mul__(self, other):
        # multiply all my resources by {other}
        return type(self)(other*r for r in self)

    def __rmul__(self, other):
        # multiply all my resources by {other}
        return type(self)(other*r for r in self)


# end of file

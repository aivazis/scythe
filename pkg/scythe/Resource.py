# -*- Python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 2018-2019 all rights reserved
#


class Resource(tuple):
    """
    The game resources
    """


    # access
    @property
    def gold(self):
        # get my gold content
        return self[0]

    @property
    def oil(self):
        # get my gold content
        return self[1]

    @property
    def wood(self):
        # get my gold content
        return self[2]

    @property
    def food(self):
        # get my gold content
        return self[3]


    # arithmetic
    def __add__(self, other):
        # go through my resources and {other}'s and add them together
        return type(self)(r1+r2 for r1, r2 in zip(self, other))

    def __sub__(self, other):
        # subtract {other}'s resources from mine
        return type(self)(r1-r2 for r1, r2 in zip(self, other))

    def __mul__(self, other):
        # multiply all my resources by {other}
        return type(self)(other*r for r in self)

    def __rmul__(self, other):
        # multiply all my resources by {other}
        return type(self)(other*r for r in self)


# constants
gold = Resource((1,0,0,0))
oil = Resource((0,1,0,0))
wood = Resource((0,0,1,0))
food = Resource((0,0,0,1))


# end of file

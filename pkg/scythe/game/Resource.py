# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# support
import journal


# base representation for game resources
class Resource(tuple):
    """
    The base class for game resources
    """


    # arithmetic; there are no in-place versions since tuples are read-only
    # combine two instance to make a new one
    def __add__(self, other):
        # type check
        if type(other) is not type(self):
            # make a channel
            channel = journal.firewall("scythe.resources")
            # and complain
            channel.log(f"can't add {other.__class__.__name__} to {self.__class__.__name__}")
        # go through my resources and {other}'s and add them together
        return type(self)(r1+r2 for r1, r2 in zip(self, other))


    def __sub__(self, other):
        if type(other) is not type(self):
            # make a channel
            channel = journal.firewall("scythe.resources")
            # and complain
            channel.log(f"can't subtract {other.__class__.__name__} from {self.__class__.__name__}")
        # subtract {other}'s resources from mine
        result = type(self)(r1-r2 for r1, r2 in zip(self, other))
        # check that there are no negative entries
        if tuple(filter(lambda x: x < 0, result)):
            # which is an error
            channel = journal.firewall("scythe.resources")
            # that must be reported
            channel.line(f"while subtracting {other} from {self}:")
            channel.log(f"negative resources are not allowed")
        # if all is good, return the result
        return result


    # scalar multiplication
    def __mul__(self, other):
        # type check
        if type(other) is not int:
            # make a channel
            channel = journal.firewall("scythe.resources")
            # and complain
            channel.log(f"can't multiply {self.__class__} by {other.__class__}")
        # multiply all my resources by {other}
        return type(self)(other*r for r in self)


    def __rmul__(self, other):
        # type check
        if type(other) is not int:
            # make a channel
            channel = journal.firewall("scythe.resources")
            # and complain
            channel.log(f"can't multiply {self.__class__} by {other.__class__}")
        # multiply all my resources by {other}
        return type(self)(other*r for r in self)


# end of file

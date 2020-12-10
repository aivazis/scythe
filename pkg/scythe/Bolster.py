# -*- Python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


class Bolster:
    """
    The "bolster" top action
    """

    # constants
    from .Resource import gold

    # public data
    @property
    def cost(self):
        """
        The cost of the move
        """
        # one gold
        return self.gold


# end of file

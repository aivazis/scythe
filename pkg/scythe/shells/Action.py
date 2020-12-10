# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# support
import pyre


# wrap over the base protocol just so we establish the local namespace
class Action(pyre.action, family="scythe.cli"):
    """
    The protocol for scythe commands
    """


# end of file

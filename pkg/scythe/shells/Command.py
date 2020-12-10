# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# support
import pyre
# the action protocol
from .Action import Action as action


# the base class for all command line panels
class Command(pyre.panel(), implements=action):
    """
    The base class for all {scythe} command panels
    """


# end of file

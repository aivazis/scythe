# -*- Python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 2018-2019 all rights reserved
#


"""
scythe is a python simulation of the board game by the same name
"""

# publich
from . import (
    meta,
)

# publish the resource types
from .Resource import gold, oil, wood, food


# administrative
def copyright():
    """
    Return the pyre copyright note
    """
    return print(meta.header)


def license():
    """
    Print the pyre license
    """
    # print it
    return print(meta.license)


def version():
    """
    Return the pyre version
    """
    return meta.version


def credits():
    """
    Print the acknowledgments
    """
    # print it
    return print(meta.acknowledgments)


# end of file

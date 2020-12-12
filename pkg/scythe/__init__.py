# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


"""
scythe is a python simulation of the board game by the same name
"""

# import and publish pyre symbols
from pyre import (
    # protocols, components, traits, and their infrastructure
    schemata, constraints, properties, protocol, component, foundry,
    # decorators
    export, provides,
    # the manager of the pyre runtime
    executive,
)


# register the package with the framework
package = executive.registerPackage(name='ampcor', file=__file__)
# save the geography
home, prefix, defaults = package.layout()


# publish the local modules
from . import meta
from . import shells
from . import cli
from . import game


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

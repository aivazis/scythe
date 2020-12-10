# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# get support
import pyre
# and my package
import scythe


# the plexus is the command center for the user interface
class Scythe(pyre.plexus, family="scythe.shells.plexus"):
    """
    The main dispatcher of user actions
    """

    # types
    from .Action import Action as pyre_action


    # pyre framework hooks
    # support for the help system
    def pyre_banner(self):
        """
        Generate the help banner
        """
        # show the license header
        return scythe.meta.license


    # interactive session management
    def pyre_interactiveSessionContext(self, context=None):
        """
        Go interactive
        """
        # prime the execution context
        context = context or {}
        # grant access to my package
        context['scythe'] = scythe  # my package
        # and chain up
        return super().pyre_interactiveSessionContext(context=context)


# end of file

# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# base class
from .Resource import Resource


# land resources are stored on a hex and belong to whichever faction currently owns the hex
class LandResource(Resource):
    """
    The game resources that are stored on land
    """


    # access
    @property
    def food(self):
        """
        Get my food content
        """
        return self[0]


    @property
    def metal(self):
        """
        Get my metal content
        """
        return self[1]

    @property
    def oil(self):
        """
        Get my oil content
        """
        return self[2]

    @property
    def wood(self):
        """
        Get my wood content
        """
        return self[3]


    # interface
    def resources(self):
        """
        Add up all resources, regardless of type; useful for end-game scoring
        """
        # easy enough
        return sum(self)


# constants: the units of the four types of land resources
food = LandResource((1,0,0,0))
metal = LandResource((0,1,0,0))
oil = LandResource((0,0,1,0))
wood = LandResource((0,0,0,1))


# end of file

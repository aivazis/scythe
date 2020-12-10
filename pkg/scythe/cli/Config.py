# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# support
import scythe


# declaration
class Config(scythe.shells.command, family="scythe.cli.config"):
    """
    Display configuration information about this package
    """


    # version info
    @scythe.export(tip="the version information")
    def version(self, **kwds):
        """
        Print the version of the scythe package
        """
        # print the version number
        print(f"{scythe.meta.version}")
        # all done
        return 0


    # configuration
    @scythe.export(tip="the top level installation directory")
    def prefix(self, **kwds):
        """
        Print the top level installation directory
        """
        # print the version number
        print(f"{scythe.prefix}")
        # all done
        return 0


    @scythe.export(tip="the directory with the executable scripts")
    def path(self, **kwds):
        """
        Print the location of the executable scripts
        """
        # print the version number
        print(f"{scythe.prefix}/bin")
        # all done
        return 0


    @scythe.export(tip="the directory with the python packages")
    def pythonpath(self, **kwds):
        """
        Print the directory with the python packages
        """
        # print the version number
        print(f"{scythe.home.parent}")
        # all done
        return 0


    @scythe.export(tip="the location of the {scythe} headers")
    def incpath(self, **kwds):
        """
        Print the locations of the {scythe} headers
        """
        # print the version number
        print(f"{scythe.prefix}/include")
        # all done
        return 0


    @scythe.export(tip="the location of the {scythe} libraries")
    def libpath(self, **kwds):
        """
        Print the locations of the {scythe} libraries
        """
        # print the version number
        print(f"{scythe.prefix}/lib")
        # all done
        return 0


# end of file

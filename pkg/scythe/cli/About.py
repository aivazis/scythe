# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# support
import scythe


# declaration
class About(scythe.shells.command, family='scythe.cli.about'):
    """
    Display information about this application
    """


    @scythe.export(tip="print the copyright note")
    def copyright(self, plexus, **kwds):
        """
        Print the copyright note of the scythe package
        """
        # show the copyright note
        plexus.info.log(scythe.meta.copyright)
        # all done
        return


    @scythe.export(tip="print out the acknowledgments")
    def credits(self, plexus, **kwds):
        """
        Print out the license and terms of use of the scythe package
        """
        # make some space
        plexus.info.log(scythe.meta.header)
        # all done
        return


    @scythe.export(tip="print out the license and terms of use")
    def license(self, plexus, **kwds):
        """
        Print out the license and terms of use of the scythe package
        """
        # make some space
        plexus.info.log(scythe.meta.license)
        # all done
        return


    @scythe.export(tip="print the version number")
    def version(self, plexus, **kwds):
        """
        Print the version of the scythe package
        """
        # make some space
        plexus.info.log(scythe.meta.header)
        # all done
        return


# end of file

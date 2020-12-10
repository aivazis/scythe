# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# support
import scythe


# the debug command displays application internals
class Debug(scythe.shells.command, family='scythe.cli.debug'):
    """
    Display debugging information about this application
    """


    # user configurable state
    prefix = scythe.properties.str()
    prefix.tip = "specify the portion of the namespace to display"


    @scythe.export(tip="dump the application configuration namespace")
    def nfs(self, plexus, **kwds):
        """
        Dump the application configuration namespace
        """
        # get the prefix
        prefix = self.prefix or "scythe"
        # show me
        plexus.pyre_nameserver.dump(prefix)
        # all done
        return 0


    @scythe.export(tip="dump the application configuration namespace")
    def vfs(self, plexus, **kwds):
        """
        Dump the application virtual filesystem
        """
        # get the prefix
        prefix = self.prefix or '/scythe'
        # build the report
        report = '\n'.join(plexus.vfs[prefix].dump())
        # sign in
        plexus.info.line('vfs: prefix={!r}'.format(prefix))
        # dump
        plexus.info.log(report)
        # all done
        return 0


# end of file

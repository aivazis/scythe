#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


def test():
    """
    Sanity test: verify the package is accessible
    """
    # try to import
    import scythe
    # all good
    return 0


# main
if __name__ == "__main__":
    # run the test
    status = test()
    # share the result
    raise SystemExit(status)


# end of file

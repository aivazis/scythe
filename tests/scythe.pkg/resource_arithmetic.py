#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


def test():
    """
    Verify that base resource arithmetic works as expected
    """
    # get the base resource
    from scythe.game.Resource import Resource as resource

    # invent one
    ones = resource((1,1,1))
    # and another
    twos = resource((2,2,2))

    # addition
    threes = ones + twos
    # check
    assert threes == (3,3,3)

    # scalar multiplication from the left
    assert 3*ones == threes
    # and from the right
    assert ones*3 == threes

    # adding
    try:
        # naked tuple
        ones + (2,2,2)
        # should fail, so this is unreachable
        assert False
    # if it did
    except:
        # no problem
        pass

    # all good
    return 0


# main
if __name__ == "__main__":
    # get the journal
    import journal
    # so we can quiet it down
    journal.quiet()

    # run the test
    status = test()
    # share the result
    raise SystemExit(status)


# end of file

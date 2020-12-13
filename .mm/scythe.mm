# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# scythe consists of a python package
scythe.packages := scythe.pkg
# libraries
scythe.libraries :=
# python extensions
scythe.extensions :=
# and some tests
scythe.tests := scythe.pkg.tests

# the scythe package meta-data
scythe.pkg.stem := scythe
scythe.pkg.drivers := scythe


# load the test suites
include $(scythe.tests)


# end of file

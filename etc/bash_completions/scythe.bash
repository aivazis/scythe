# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@orthologue.com>
# (c) 2018-2020 all rights reserved


# bash completion script for scythe

function _scythe() {
    # get the partial command line
    local line=${COMP_LINE}
    local word=${COMP_WORDS[COMP_CWORD]}
    # ask scythe to provide guesses
    COMPREPLY=($(scythe complete --word="${word}" --line="${line}"))
}

# register the hook
complete -F _scythe scythe


# end of file

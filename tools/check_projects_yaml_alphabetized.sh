#!/bin/bash -xe

# Checks that reference/projects.yaml alphabetized and prints list of
# projects that should be sorted.

export TMPDIR=$(mktemp -d tox.XXXXXX)
trap "rm -rf $TMPDIR" EXIT

pushd $TMPDIR
PROJECTS_LIST=$OLDPWD/reference/tsc/projects.yaml

grep '^[a-zA-Z0-9]' $PROJECTS_LIST > projects_list

LC_ALL=C sort --ignore-case projects_list -o projects_list.sorted

if ! diff projects_list projects_list.sorted > projects_list.diff; then
    echo "The following projects should be alphabetized: "
    cat projects_list.diff | grep -e '> '
    exit 1
else
    echo "Projects alphabetized"
fi

popd

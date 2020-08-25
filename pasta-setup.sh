#! /bin/bash

# Author:
#   Rohit Sarkar <rohitsarkar5398@gmail.com>
#
# This work is licensed under the terms of the GNU GPL, version 2.  See
# the COPYING file in the top-level directory.

set -e

LIST_ADDR=$1
PROJECT=$(echo $LIST_ADDR | sed -e 's/\(.*\)@.*/\1/')
MBOX=./${LIST_ADDR}.mbox

python create-project.py $LIST_ADDR
./manage.py parsearchive $MBOX --list-id $PROJECT
./manage.py dumparchive $PROJECT
tar -xvf *.tar
rm -f *.tar

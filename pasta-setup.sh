#! /bin/bash

# Author:
#   Rohit Sarkar <rohitsarkar5398@gmail.com>
#
# This work is licensed under the terms of the GNU GPL, version 2.  See
# the COPYING file in the top-level directory.

set -e

python create-project.py $2
./manage.py parsearchive $1 --list-id $2
./manage.py dumparchive $2
tar -xf *.tar
rm -f *.tar

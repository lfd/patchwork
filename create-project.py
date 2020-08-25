# Author:
#   Rohit Sarkar <rohitsarkar5398@gmail.com>
#
# This work is licensed under the terms of the GNU GPL, version 2.  See
# the COPYING file in the top-level directory.

import sys

def create_project(name, listemail):
    if exists(name):
        print('Project %s already exists' % name)
        return
    print('Creating project %s' % name)
    new_project = Project.objects.create(linkname=name,
            name=name,
            listid=name,
            listemail=listemail)

def exists(project_name):
    return len(Project.objects.filter(linkname=project_name)) > 0

def find_project_id(name):
    project = Project.objects.get(linkname=name)
    return project.id


if __name__ == '__main__':
    list_addr = sys.argv[1]
    project_name = list_addr.split('@')[0]

    import django
    django.setup()

    from patchwork.models import Project
    create_project(project_name, list_addr)

    with open('project_id', 'w+') as f:
        f.write(str(find_project_id(project_name)))

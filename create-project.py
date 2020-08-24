# Author:
#   Rohit Sarkar <rohitsarkar5398@gmail.com>
#
# This work is licensed under the terms of the GNU GPL, version 2.  See
# the COPYING file in the top-level directory.

def create_project(name):
    if exists(name):
        print('Project %s already exists' % name)
        return
    print('Creating project %s' % name)
    new_project = Project.objects.create(linkname=name,
            name=name,
            listid=name,
            listemail='{0}@{0}.com'.format(name))

def exists(project_name):
    return len(Project.objects.filter(linkname=project_name)) > 0

def find_project_id(name):
    project = Project.objects.get(linkname=name)
    return project.id


if __name__ == '__main__':
    import django
    django.setup()
    from patchwork.models import Project
    import sys
    create_project(sys.argv[1])
    with open('project_id', 'w+') as f:
        f.write(str(find_project_id(sys.argv[1])))

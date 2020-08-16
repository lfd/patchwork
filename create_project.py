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


if __name__ == '__main__':
    import django
    django.setup()
    from patchwork.models import Project
    import sys
    create_project(sys.argv[1])

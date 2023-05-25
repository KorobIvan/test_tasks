import yaml
from docopt import docopt

usage = '''
Usage:
app.py list <file> [dir]
app.py get <file> <name> [dir]
'''

with open('tasks.yaml') as f:
    tasks = yaml.safe_load(f)

with open('builds.yaml') as f:
    builds = yaml.safe_load(f)

def list_from_file(file):
    if file == 'tasks':
        print('List of available builds:')
        for i in tasks['tasks']:
            print(f'* {i["name"]}')
    elif file == 'builds':
        print('List of available builds:')
        for i in builds['builds']:
            print(f'* {i["name"]}')
    else:
        print('Typy of work NOT found!')


def get_info(file, name):
    if file == 'tasks':
        for i in tasks['tasks']:
            if i['name'] == name:
                print('Task info:')
                print(f'* name: {i["name"]}\n\
* dependencies: {", ".join(i["dependencies"])}')
                break
        else:
            print('Name eror')   
    elif file == 'builds':
        for i in builds['builds']:
            if i['name'] == name:
                print('Task info:')
                print(f'* name: {i["name"]}\n\
* tasks: {", ".join(i["tasks"])}')
                break
        else:
            print('Name eror')
             
    else:
        print('Type of work NOT found!')        


args = docopt(usage)




'''if args['<path>'] != None:
    path = args['<path>']'''



if args['list']:
    if args['<file>'] != None:
        list_from_file(args['<file>'])
elif args['get']:
    if args['<file>'] != None and args['<name>'] != None:
        get_info(args['<file>'], args['<name>'])



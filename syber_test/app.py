import yaml
from docopt import docopt

usage = '''
Usage:
app.py list <file> [<dir>]
app.py get <file> <name> [<dir>]
'''

def list_from_file(work_type, path=''):
    try:
        with open(f'{path}{work_type}.yaml') as f:
            file = yaml.safe_load(f)
        work = 'List of available builds:'
        for i in file[work_type]:
            work += f'\n* {i["name"]}'
        return work
    except FileNotFoundError:
        return 'File not found!'


def get_info(work_type, name, path=''):
    try: 
        with open(f'{path}{work_type}.yaml') as f:
            file = yaml.safe_load(f)  
        for i in file[work_type]:
            data = list(i.keys())
            if i['name'] == name:
                return f'Task info:\n* name: {i["name"]}\n\
* {data[1]}: {", ".join(i[data[1]])}'
        else:
            return 'Name eror!'         
    except FileNotFoundError:
        return 'File not found!'


def main():
    try:
        args = docopt(usage)
        path = ''
        
        if args['<dir>'] != None:
            path = args['<dir>'] + '\\'

        if args['list']:
            if args['<file>'] != None:
                return list_from_file(args['<file>'], path)
        elif args['get']:
            if args['<file>'] != None and args['<name>'] != None:
                return get_info(args['<file>'], args['<name>'], path)
    except:
        return 'Command not found!'


if __name__ == '__main__':
    print(main())

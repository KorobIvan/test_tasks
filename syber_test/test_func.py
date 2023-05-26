import yaml
import pytest
from app import get_info, list_from_file
import subprocess


def test_command_true():
    assert subprocess.call("python app.py list tasks", shell=True) != 'Command not found!'
    assert subprocess.call("python app.py list builds", shell=True) != 'Command not found!'

def test_get_true():
    with open('builds.yaml') as f:
        builds = yaml.safe_load(f)
        
        for i in builds['builds']:
            res = f'Task info:\n* name: {i["name"]}\n* tasks: {", ".join(i["tasks"])}'
            assert get_info('builds', i['name']) == res

    with open('tasks.yaml') as f:
        tasks = yaml.safe_load(f)

        for i in tasks['tasks']:
            res = f'Task info:\n* name: {i["name"]}\n* dependencies: {", ".join(i["dependencies"])}'
            assert get_info('tasks', i['name']) == res

def test_get_false():
    assert get_info('builds', '') != 'Task info:\n* name: audience_stand\n* tasks: enable_fuchsia_fairies, read_blue_witches, upgrade_olive_gnomes'
    assert get_info('tasks', 'build_lime_cyclops') != 'bring_purple_leprechauns'

def test_list_true():
    with open('builds.yaml') as f:
        builds = yaml.safe_load(f)
        for i in builds['builds']:
            assert i["name"] in list_from_file('builds')

    with open('tasks.yaml') as f:
        tasks = yaml.safe_load(f)
        for i in tasks['tasks']:
            assert i["name"] in list_from_file('tasks')

def test_list_false():
    assert 'create_lovely_cyclops' not in list_from_file('tasks')
    assert 'create_lovely_cyclops' not in list_from_file('builds')



test = pytest.main()
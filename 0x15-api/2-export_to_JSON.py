#!/usr/bin/python3
""" Uses a REST API, fetching data about a given employee
    (identified by their id passed to sript as argument) &
    exports the data (of all tasks owned by user) in the JSON format
"""
import json
import requests
import sys


if __name__ == '__main__':
    # get the data
    if len(sys.argv) > 1:
        api = 'https://jsonplaceholder.typicode.com/'
        user = requests.get(api + 'users/{}'.format(sys.argv[1]))
        todos = requests.get(api + 'todos')
        user_todos = []
        for todo in todos.json():
            if todo.get('userId') == int(sys.argv[1]):
                user_todos.append(todo)
        file_name = '{}.json'.format(sys.argv[1])
        username = user.json().get('username')
        with open(file_name, 'w') as f:
            todo_list = []
            for todo in user_todos:
                dict_ = {}
                dict_['task'] = todo.get('title')
                dict_['completed'] = todo.get('completed')
                dict_['username'] = username
                todo_list.append(dict_)
            to_dump = {}
            to_dump[sys.argv[1]] = todo_list
            json.dump(to_dump, f)

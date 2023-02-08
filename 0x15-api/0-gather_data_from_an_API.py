#!/usr/bin/python3
""" Uses a REST API, fetching data about a given employee
    (identified by their id passed in as an arg).
    Returns:
            information about thir TODO list progress
    Requirements:
            must use urllib or requests module
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # get the info
        api = 'https://jsonplaceholder.typicode.com/'
        user = requests.get(api + 'users/{}'.format(sys.argv[1]))
        todos = requests.get(api + 'todos')
        # print(user.json().get('name'))
        user_todos = []
        completed = 0
        todos = todos.json()
        for todo in todos:
            if todo.get('userId') == int(sys.argv[1]):
                user_todos.append(todo)
                if todo.get('completed'):
                    completed += 1
        print('Employee {} is done with tasks({}/{}):'
              .format(user.json().get('name'), completed, len(user_todos)))
        for todo in user_todos:
            print('\t {}'.format(todo.get('title')))

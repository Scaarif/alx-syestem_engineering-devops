#!/usr/bin/python3
""" Uses a REST API, fetching data about a given employees &
    exports the data (each user and their tasks ) in the JSON format
"""
import json
import requests
import sys


if __name__ == '__main__':
    # get the data
    api = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(api + 'users')
    todos = requests.get(api + 'todos')
    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as f:
        # for each user, get their todos and add to dict [user_id]
        to_dump = {}
        for user in users.json():
            user_todos = []
            for todo in todos.json():
                dict_ = {}
                if todo.get('userId') == user.get('id'):
                    dict_['username'] = user.get('username')
                    dict_['task'] = todo.get('title')
                    dict_['completed'] = todo.get('completed')
                    user_todos.append(dict_)
            to_dump[user.get('id')] = user_todos
        # dump the dictionary of user and their todos list
        json.dump(to_dump, f)

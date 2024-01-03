#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    import json
    import requests
    import sys

    tds = requests.get('https://jsonplaceholder.typicode.com/todos')
    usr = requests.get("https://jsonplaceholder.typicode.com/users")
    tds = tds.json()
    usr = usr.json()
    todoAll = {}

    for user in usr:
        taskList = []
        for task in tds:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)

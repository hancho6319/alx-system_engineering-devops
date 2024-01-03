#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import json
from sys import argv
import urllib.request

if __name__ == "__main__":
    emp_id = argv[1]
    url_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    url_id = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(emp_id)

    with urllib.request.urlopen(url_id) as response_id, urllib.request.urlopen(url_name) as response_name:
        employee = json.loads(response_id.read().decode())
        employeeName = json.loads(response_name.read().decode())

    name = employeeName['name']

    totalTasks = sum(1 for done_task in employee if done_task['completed'])

    print("Employee {} is done with tasks({}/{}):".format(name, totalTasks, len(employee)))

    for done_task in employee:
        if done_task['completed']:
            print("\t " + done_task.get('title'))

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
    url_name = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    url_id = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'

    with urllib.request.urlopen(url_id) as response_id, \
            urllib.request.urlopen(url_name) as response_name:
        employee = json.loads(response_id.read().decode())
        employeeName = json.loads(response_name.read().decode())

    name = employeeName['name']

    totalTasks = sum(1 for done_task in employee if done_task['completed'])

    print(f"Employee {name} is done with tasks({totalTasks}/{len(employee)}):")

    for done_task in employee:
        if done_task['completed']:
            print("\t " + done_task.get('title'))

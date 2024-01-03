#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""

import json
import urllib.request
from sys import argv

if __name__ == "__main__":
    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    with urllib.request.urlopen(idURL) as response_id, \
            urllib.request.urlopen(nameURL) as response_name:
        employee = json.loads(response_id.read().decode())
        employeeName = json.loads(response_name.read().decode())

    usr = employeeName['username']

    totalTasks = []

    for all_Emp in employee:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })

    updateUser = {idEmp: totalTasks}

    file_Json = idEmp + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)

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
    api_users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    api_todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    
    all_employee_tasks = {}

    for user in api_users:
        user_tasks = []
        for task in api_todos:
            if task.get('userId') == user.get('id'):
                task_info = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                user_tasks.append(task_info)
        all_employee_tasks[user.get('id')] = user_tasks

    with open('all_employees_tasks.json', mode='w') as json_file:
        json.dump(all_employee_tasks, json_file)

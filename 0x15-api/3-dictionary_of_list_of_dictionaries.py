#!/usr/bin/python3
"""
Script that retrieves data from a REST API 
for employee TODO lists
and exports the information in JSON format.
"""

import json
import requests
from sys import argv

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def generate_employee_tasks(users_data, todos_data):
    employee_tasks = {}

    for user in users_data:
        user_tasks = []
        for task in todos_data:
            if task.get('userId') == user.get('id'):
                task_info = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                user_tasks.append(task_info)
        employee_tasks[user.get('id')] = user_tasks

    return employee_tasks

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_data = fetch_data(users_url)
    todos_data = fetch_data(todos_url)

    if users_data and todos_data:
        all_employee_tasks = generate_employee_tasks(users_data, todos_data)

        with open('all_employees_tasks.json', mode='w') as json_file:
            json.dump(all_employee_tasks, json_file)
            print("Data successfully exported to 'all_employees_tasks.json'")
    else:
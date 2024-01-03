#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""

import json
import requests
from sys import argv

def fetch_data(url):
    try:
        with requests.Session() as sessionReq:
            response = sessionReq.get(url)
            response.raise_for_status()  # Raise an exception for 4XX/5XX status codes
            return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    if len(argv) < 2:
        print("Please provide an employee ID.")
    else:
        employee_id = argv[1]
        tasks_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

        tasks_data = fetch_data(tasks_url)
        user_data = fetch_data(user_url)

        if tasks_data and user_data:
            user_name = user_data['username']
            total_tasks = []

            for task in tasks_data:
                total_tasks.append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user_name,
                })

            update_user = {employee_id: total_tasks}
            file_json = f"{employee_id}.json"

            with open(file_json, 'w') as file:
                json.dump(update_user, file)
                print(f"Data for employee {employee_id} written to {file_json}")

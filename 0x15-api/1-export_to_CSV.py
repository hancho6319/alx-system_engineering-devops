import json
import urllib.request
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    url_id = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    url_name = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    with urllib.request.urlopen(url_id) as response_id, \
            urllib.request.urlopen(url_name) as response_name:
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

    updateUser = {emp_id: totalTasks}

    file_Json = emp_id + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)

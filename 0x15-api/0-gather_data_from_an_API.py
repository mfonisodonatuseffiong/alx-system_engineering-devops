#!/usr/bin/python3
"""
Gather employee data from API.
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            req = requests.get(f'{REST_API}/users/{employee_id}').json()
            task_req = requests.get(f'{REST_API}/todos').json()
            emp_name = req.get('name')
            tasks = [task for task in task_req if task.get('userId') == employee_id]
            completed_tasks = [task for task in tasks if task.get('completed')]
            print(
                f'Employee {emp_name} is done with tasks({len(completed_tasks)}/{len(tasks)}):'
            )
            for task in completed_tasks:
                print(f'\t {task.get("title")}')

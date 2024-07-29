#!/usr/bin/python3
"""
Gather employee data from API.
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def fetch_data(employee_id):
    """Fetch employee and task data from the API."""
    try:
        user_response = requests.get(f'{REST_API}/users/{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()
        
        todo_response = requests.get(f'{REST_API}/todos')
        todo_response.raise_for_status()
        todos = todo_response.json()

        return user_data, todos
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        employee_id = int(sys.argv[1])
        user_data, todos = fetch_data(employee_id)
        
        emp_name = user_data.get('name')
        tasks = [task for task in todos if task.get('userId') == employee_id]
        completed_tasks = [task for task in tasks if task.get('completed')]

        print(f'Employee {emp_name} is done with tasks '
              f'({len(completed_tasks)}/{len(tasks)}):')
        for task in completed_tasks:
            print(f'\t {task.get("title")}')
    else:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

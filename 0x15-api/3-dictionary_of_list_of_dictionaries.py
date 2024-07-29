#!/usr/bin/python3
"""Python script to fetch REST API for todo lists of employees."""

import json
import requests
import sys


def fetch_user_data():
    """Fetch user data from the API."""
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching user data: {e}")
        sys.exit(1)


def fetch_tasks(user_id):
    """Fetch tasks for a specific user from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching tasks for user {user_id}: {e}")
        sys.exit(1)


def main():
    """Main function to gather data and write to a JSON file."""
    users = fetch_user_data()
    users_dict = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = fetch_tasks(user_id)

        users_dict[user_id] = []

        for task in tasks:
            task_title = task.get('title')
            task_completed = task.get('completed')
            users_dict[user_id].append({
                "task": task_title,
                "completed": task_completed,
                "username": username
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f, indent=4)


if __name__ == '__main__':
    main()


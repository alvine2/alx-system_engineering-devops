#!/usr/bin/python3
"""Python script to fetch REST API for todo lists of employees"""

import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(url)
    users = resp.json()

    users_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

        resp = requests.get(todos_url)
        tasks = resp.json()

        users_dict[user_id] = []
        for task in tasks:
            task_completed_status = task.get('completed')
            task_title = task.get('title')
            users_dict[user_id].append({
                "task": task_title,
                "completed": task_completed_status,
                "username": username
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f, indent=4)  # Added indent for better readability


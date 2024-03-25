#!/usr/bin/python3
"""Python script that, using this REST API, for all employee"""

import json
import requests


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'

    response = requests.get(users_url)
    users = response.json()

    all_tasks = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']

        todos_url = f'{base_url}/todos?userId={user_id}'
        response_todos = requests.get(todos_url)
        todos = response_todos.json()

        user_tasks = []
        for todo in todos:
            task = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            user_tasks.append(task)

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

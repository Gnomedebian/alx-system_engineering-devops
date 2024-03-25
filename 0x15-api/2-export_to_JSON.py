#!/usr/bin/python3
"""Py script to export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    response = requests.get('{}/todos?userId={}'.format(
                            BASE_URL, employee_id))
    todos = response.json()

    response_user = requests.get('{}/users/{}'.format(
                            BASE_URL, employee_id))
    user_info = response_user.json()
    employee_name = user_info['name']

    data = {employee_id: []}

    for todo in todos:
        task_info = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': employee_name
                }
        data[employee_id].append(task_info)

    filename = '{}.json'.format(employee_id)

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

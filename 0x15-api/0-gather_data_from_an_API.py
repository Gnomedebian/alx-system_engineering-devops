#!/usr/bin/python3

"""Returns todo list information for a given employee ID, using REST api"""

import requests
import sys

if __name__ == "__main__":

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    response = requests.get('{}/todos?userId={}'.format(BASE_URL, employee_id))
    todos = response.json()

    response_user = requests.get('{}/users/{}'.format(BASE_URL, employee_id))
    user_info = response_user.json()
    employee_name = user_info['name']

    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
            employee_name, num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task['title']))

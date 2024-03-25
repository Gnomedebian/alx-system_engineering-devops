#!/usr/bin/python3
"""Exports todo list information for a given employee ID to CSV format"""
import csv
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

    filename = '{}.csv'.format(employee_id)

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, quotechar='"')
        for todo in todos:
            csv_writer.writerow([employee_id, employee_name,
                                todo['completed'], todo['title']])

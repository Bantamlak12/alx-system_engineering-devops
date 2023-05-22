#!/usr/bin/python3
""" A Python script that, using this https://jsonplaceholder.typicode.com/
    REST API for a given employee ID, returns information about his/her
    TODO listprogress.
"""
import requests
import sys


if __name__ == "__main__":
    # Get employee id from command line
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    # Get information about the employee
    response = requests.get(url)
    employee_name = response.json().get('name')

    # Get information about the employee todo list
    response = requests.get("{}/todos".format(url))
    todo_list = response.json()

    # Get number of total tasks
    total_tasks = len(todo_list)

    # Get list of completed tasks
    completed_tasks = []
    for task in todo_list:
        if task.get('completed') is True:
            completed_tasks.append(task)
    # Get number of completed tasks
    total_completed_tasks = len(completed_tasks)

    # Print out his/her todo list progress
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
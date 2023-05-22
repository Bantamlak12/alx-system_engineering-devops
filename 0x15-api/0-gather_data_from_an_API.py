#!/usr/bin/python3
""" A Python script that uses REST API to retrieve todo listprogress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    response = requests.get(url)
    employee_name = response.json().get('name')

    response = requests.get("{}/todos".format(url))
    todo_list = response.json()

    completed_tasks = []
    for task in todo_list:
        if task.get('completed') is True:
            completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(completed_tasks), len(todo_list)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

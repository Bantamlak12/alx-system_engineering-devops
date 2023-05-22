#!/usr/bin/python3
"""Extends task #0 Python script to export data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    filename = "{}.csv".format(user_id)

    response = requests.get(url)
    username = response.json().get('username')

    response = requests.get("{}/todos".format(url))
    todo_list = response.json()

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([user_id, username, task.get('completed'),
                            task.get('title')])

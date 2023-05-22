#!/usr/bin/python3
"""Extends task #0 Python script to export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    filename = "todo_all_employees.json"

    response = requests.get(url)
    users = response.json()

    data = {}

    for user in users:
        user_id = user.get('id')
        data[user_id] = []

        response = requests.get("{}/{}/todos".format(url, user_id))
        todo_list = response.json()
        for t in todo_list:
            user_data = {
                    "username": user.get('username'),
                    "task": t.get('title'),
                    "completed": t.get('completed')
            }
            data.get(user_id).append(user_data)

    with open(filename, "w") as json_file:
        json.dump(data, json_file)

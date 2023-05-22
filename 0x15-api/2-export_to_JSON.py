#!/usr/bin/python3
"""Extends task #0 Python script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    filename = "{}.json".format(user_id)

    response = requests.get(url)
    username = response.json().get('username')

    response = requests.get("{}/todos".format(url))
    todo_list = response.json()

    data = {
            user_id: []
        }

    for t in todo_list:
        user_data = {
                "task": t.get('title'),
                "completed": t.get('completed'),
                "username": username
        }

    data.get(user_id).append(user_data)

    with open(filename, "w") as json_file:
        json.dump(data, json_file)

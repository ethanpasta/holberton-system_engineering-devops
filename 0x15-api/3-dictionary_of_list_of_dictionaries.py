#!/usr/bin/python3
""" Module for task 3 """

if __name__ == "__main__":
    import json
    import requests

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    json_dic = {}
    for user in users:
        todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(user.get("id"))).json()
        json_dic["{}".format(user.get("id"))] = [
            {"task": task.get("title"),
             "completed": task.get("completed"),
             "username": user.get("username")} for task in todo]
        with open('todo_all_employees.json'.format(
                user.get("id")), mode='w') as f:
            json.dump(json_dic, f)

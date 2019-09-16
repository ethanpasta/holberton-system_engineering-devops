#!/usr/bin/python3
""" Module for task 2 """
import json
import requests
from sys import argv

user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(argv[1])).json()
username = user.get("username")
todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                    .format(argv[1])).json()
json_dic = {}
json_dic["{}".format(user.get("id"))] = [
    {"task": task.get("title"),
     "completed": task.get("completed"),
     "username": username} for task in todo]
with open('{}.json'.format(user.get("id")), mode='w') as f:
    json.dump(json_dic, f)

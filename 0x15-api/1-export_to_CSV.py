#!/usr/bin/python3
""" Module for task 1 """
import csv
import requests
from sys import argv

user_id = argv[1]
user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(user_id)).json()
username = user.get("username")
todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                    .format(user_id)).json()
with open("{}.csv".format(user_id), mode='w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
    for task in todo:
        csv_writer.writerow([user_id, username, task.get("completed"),
                             task.get("title")])

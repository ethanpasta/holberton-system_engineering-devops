#!/usr/bin/python3
""" Module for task 0 """

if __name__ == "__main__":
    import requests
    from sys import argv

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()
    todo_complete = [todo_m for todo_m in todo if todo_m.get("completed")]
    print("Employee {} is done with tasks({}/{})".format(user.get("name"),
                                                         len(todo_complete),
                                                         len(todo)))
    for task in todo_complete:
        print('\t {}'.format(task.get("title")))

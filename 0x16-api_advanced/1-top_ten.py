#!/usr/bin/python3
""" Module for task 1 """


def top_ten(subreddit):
    import requests

    headers = {
        'User-Agent': 'My-User-Agent'
    }
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code > 300:
        print("None")
    else:
        [print(d.get("data").get("title"))
         for d in r.json().get("data").get("children")]

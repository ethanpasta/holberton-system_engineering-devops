#!/usr/bin/python3
""" Module for task 0 """
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/76.0.3809.132 Safari/537.36')
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers=headers)
    try:
        return r.json()["data"]["subscribers"]
    except Exception:
        return 0

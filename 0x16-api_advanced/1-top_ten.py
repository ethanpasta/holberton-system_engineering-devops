#!/usr/bin/python3
""" Module for task 1 """
import requests


def top_ten(subreddit):
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/76.0.3809.132 Safari/537.36')
    }
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code > 300:
        print("None")
        return
    listings = r.json()["data"]["children"]
    for listing in listings:
        print(listing["data"]["title"])

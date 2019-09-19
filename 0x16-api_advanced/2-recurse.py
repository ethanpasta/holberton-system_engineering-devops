#!/usr/bin/python3
""" Module for task 1 """
import requests


def get_lists(headers, data, subreddit, hot_list=[]):
    if count == 5:
        return hot_list
    if data:
        url = "https://www.reddit.com/r/{}/top.json?after={}".format(
            subreddit, data)
    else:
        url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    try:
        r = requests.get(url, headers=headers, data=data)
        listings = r.json()
        for listing in listings["data"]["children"]:
            hot_list.append(listing["data"]["title"])
        if listings["data"]["after"] != "null":
            return get_lists(headers, listings["data"]["after"],
                             subreddit, hot_list)
        else:
            return hot_list
    except Exception:
        return None


def recurse(subreddit, hot_list=[]):
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/76.0.3809.132 Safari/537.36')
    }
    return get_lists(headers, None, subreddit, hot_list)

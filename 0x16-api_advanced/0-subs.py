#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit...
"""
import requests


def number_of_subscribers(subreddit):
    """ Return the total number of subscibers on a given subreddit... """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")

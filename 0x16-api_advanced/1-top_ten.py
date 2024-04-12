#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit

Keyword arguments:
argument -- description
Return: If not a valid subreddit, print None.
"""


def top_ten(subreddit):
    """ printting the title of the first 10 hot posts for a given subreddit."""
    url = "https://wwww.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers,
                       params=params, allow_redirect=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]

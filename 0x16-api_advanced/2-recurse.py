#!/usr/bin/python3
"""
 list containing the titles of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    if after:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                     after)
        headers = {'User-Agent': 'user agent 1.0'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data["data"]["after"]
            return recurse(subreddit, hot_list, after)
        else:
            return None
    else:
        return hot_list

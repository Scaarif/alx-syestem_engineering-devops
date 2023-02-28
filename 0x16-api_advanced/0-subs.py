#!/usr/bin/python3
""" Defines a function that queries the Reddit API and returns
    the number of subscribers (total) for a given subreddit. Function
    returns 0 if a n invalid subreddit is given
"""
import requests


def number_of_subscribers(subreddit):
    """ requests the API """
    # set a custom User-Agent
    headers = {'User-Agent': 'APIadvanced/1.0.0'}
    # set/format url (with subreddit name)
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    try:
        return res.json().get('data').get('subscribers')
    except Exception as e:
        return 0

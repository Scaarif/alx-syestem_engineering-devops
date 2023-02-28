#!/usr/bin/python3
""" Defines a function that queries the Reddit API and prints the
    first 10 hot posts listed for a given subreddit. Prints None if an
    invalid subreddit is given
"""
import requests


def top_ten(subreddit):
    # set a custom User-Agent
    headers = {'User-Agent': 'APIadvanced/1.0.0'}
    # set/format url (with subreddit name)
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers=headers, params={
                       'limit': 10}, allow_redirects=False)
    try:
        data = res.json()['data']['children']
        # print('data: ', data)
        for post in data:
            print(post['data']['title'])
    except Exception as e:
        print(None)

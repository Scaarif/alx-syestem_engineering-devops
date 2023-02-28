#!/usr/bin/python3
""" Defines a function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. Returns
    None if an invalid subreddit is given
"""
import requests


def recurse(subreddit, hot_list=[]):
    # set a custom User-Agent
    headers = {'User-Agent': 'APIadvanced/1.0.0'}
    # set/format url (with subreddit name)
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if getattr(recurse, 'more', None) is None:
        setattr(recurse, 'more', 100)
    # print(recurse.__name__, recurse.__dict__)
    if getattr(recurse, 'params', None) is None:
        setattr(recurse, 'params', {'limit': 100})
    # base case (recurse only if there are more 'things') else, return
    if (getattr(recurse, 'more') >= 100):
        res = requests.get(url, headers=headers, params=getattr(
            recurse, 'params'), allow_redirects=False)
        try:
            after = res.json()['data']['after']
            data = res.json()['data']['children']
            recurse.more = len(data)
            # print('more: ', recurse.more)
            # print('data: ', data)
            for post in data:
                # print(post['data']['title'])
                hot_list.append(post['data']['title'])
            # print(len(hot_list))
            recurse.params['after'] = after
            # print(recurse.params['after'])
            return recurse(subreddit, hot_list=hot_list)
        except Exception as e:
            # print(None)
            return None
    return hot_list


if __name__ == '__main__':
    ls = recurse('python')
    print(len(ls) if ls else None)
    print(ls[:10])
    print(ls[-10:])

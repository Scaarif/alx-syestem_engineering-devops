#!/usr/bin/python3
""" Defines a function that counts appearances of keywords in
    titles of the hottest posts in a subreddit.
"""
import requests


def count_words(subreddit, word_list):
    """
    Counts the number of appearances in of key words (in word_list)
    in the titles of the hottest posts of a subreddit.
    Print results in descending order by the count, not the title.
    If no posts match or subreddit is invalid, print a newline.
    If a word has no matches, skip and do not print it.
    """
    words = {word.lower(): 0 for word in word_list}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'APIadvanced/1.0.0'}

    r = requests.get(url, headers=headers, allow_redirects=False)
    try:
        while (1):
            r = r.json()
            for post in r['data']['children']:
                tmp = post['data']['title'].split()
                for word in tmp:
                    if word.lower() in words.keys():
                        words[word.lower()] += 1

            after = r['data']['after']
            if (after is None):
                break
            r = requests.get("{}?after={}".format(url, after),
                             headers=headers, allow_redirects=False)
    except Exception:
        pass

    words = [(k, words[k]) for k in
             sorted(words, key=words.get, reverse=True)]

    if len(words) == 0:
        print("")
    else:
        w_list = [word.lower() for word in word_list]
        for k, v in words:
            if (v > 0):
                print("{}: {:d}".format(k, v * w_list.count(k)))

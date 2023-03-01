#!/usr/bin/python3
""" Defines a function that queries the Reddit API, parses the titles
    of all hot articles for a given subreddit and prints a sorted count of
    given keywords (case-insensitive, delimited by spaces). Prints
    Nothing if an invalid subreddit is given
"""
import requests


def count_words(subreddit, word_list):
    # set a custom User-Agent
    headers = {'User-Agent': 'APIadvanced/1.0.0'}
    # set/format url (with subreddit name)
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if getattr(count_words, 'more', None) is None:
        setattr(count_words, 'more', 100)
    # print(count_words.__name__, count_words.__dict__)
    if getattr(count_words, 'params', None) is None:
        setattr(count_words, 'params', {'limit': 100})
    if getattr(count_words, 'words', None) is None:
        setattr(count_words, 'words', {})
    if getattr(count_words, 'words') == {}:
        # print('setting words attribute')
        for word in word_list:
            if word.lower() not in count_words.words.keys():
                count_words.words[word.lower()] = 0
    # base case (count_words only if there are more 'things') else, return
    if (getattr(count_words, 'more') >= 100):
        res = requests.get(url, headers=headers, params=getattr(
            count_words, 'params'), allow_redirects=False)
        # print('in loop')
        try:
            after = res.json()['data']['after']
            data = res.json()['data']['children']
            count_words.more = len(data)
            for post in data:
                # print(post['data']['title'])
                for word in word_list:
                    count_words.words[word.lower()] += (post['data']['title'].
                                                        lower().count(word.lower()))
            count_words.params['after'] = after
            return count_words(subreddit, word_list)
        except Exception as e:
            # print('error: ', e)
            pass
    # print results, in descending order, by count and if the count is same,
    # alphabetically sorted ( ascending A-Z)
    if len(word_list) > 1:
        count = sorted(count_words.words.items(), key=lambda item: item[1])
        count = dict(count)
        for key in reversed(count):
            if count[key] != 0:
                print('{}: {}'.format(key.lower(), count[key]))
    else:
        print('{}: {}'.format(word_list[0].lower(),
                              count_words.words[word_list[0].lower()]))


if __name__ == '__main__':
    # count_words('programming', ['react', 'python', 'java', 'javascript',
    #            'scala', 'no_results_for_this_one'])
    count_words('programming', ['java', 'Java'])

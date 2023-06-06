#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """ A function that queries the Reddit API and prints the titles of
        the first 10 hot posts listed.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    elif response.status_code == 404:
        print('None')
    else:
        return 0

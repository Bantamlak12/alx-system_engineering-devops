#!/usr/bin/python3
"""Number of subs"""
import requests


def number_of_subscribers(subreddit):
    """ A function that queries the Reddit API and returns the
        number of subscribers.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    elif response.status_code == 301:
        return 0
    else:
        return 0

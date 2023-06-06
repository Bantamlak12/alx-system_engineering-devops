#!/usr/bin/python3
"""Recurse it"""
import requests


def recurse(subreddit, after=None):
    """ A recursive function that queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=25&after={}'\
          .format(subreddit, after)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    data = response.json()
    articles = data['data']['children']
    if articles is None:
        return None
    titles = [article['data']['title'] for article in articles]

    # Check the next page
    after = data['data']['after']
    if after:
        next_page_title = recurse(subreddit, after)
        if next_page_title:
            titles.extend(next_page_title)

    return titles

#!/usr/bin/python3
"""
This module has function to querry hot subreddits.

the function will then print titles of the top 10 hot subreddit.
"""

import requests


def top_ten(subreddit):
    """Querry top ten hot subreddits."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {}
    header['User-Agent'] = 'api-advanced:v1.0.0 (by u/D-Murenzi)'
    parameters = {}
    parameters['limit'] = 10
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    results = response.json().get('data').get('children')

    a = 0
    while a < 10:
        print(results[a].get('data').get('title'))
        a = a + 1

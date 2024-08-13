#!/usr/bin/python3
"""
This module contains a function that returns a number of subscribers on
a given sub-reddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers to the subreddit."""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {
        }
    header['User-Agent'] = 'api-advanced:v1.0.0 (by u/D-Murenzi)'
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get('data')
    return results.get('subscribers')

#!/usr/bin/python3
"""This module has a function that recursively wuerry title of a subreddit."""
import requests


def recurse(subreddit, hot_list=[], parameters={}):
    """Return hot list in subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {}
    header['User-Agent'] = 'api-advanced:v1.0.0 (by u/D-Murenzi)'
    response = requests.get(
        url, headers=header, params=parameters, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    a = 0
    while a < len(data.get('children')):
        hot_list.append(data.get('children')[a].get('data').get('title'))
        a = a + 1
    if data.get('after') is None:
        return hot_list
    else:
        parameters['after'] = data.get('after')
        return recurse(subreddit, hot_list, parameters)

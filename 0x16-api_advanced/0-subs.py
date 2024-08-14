#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditApp/0.0.1 (by /u/your_username)"}

    try:
        sub_info = requests.get(url, headers=headers, allow_redirects=False)
        if sub_info.status_code == 200:
            data = sub_info.json().get("data", {})
            return data.get("subscribers", 0)
        return 0
    except requests.RequestException:
        return 0

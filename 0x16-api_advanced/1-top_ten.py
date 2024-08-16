#!/usr/bin/python3
"""
A script to print the titles of the top 10 hottest posts from a specified
Reddit subreddit.

Usage:
    top_ten(subreddit)

Arguments:
    subreddit (str): The name of the subreddit to query.

Description:
    This script uses the Reddit API to fetch and print the titles of the
    top 10 hottest posts from a given subreddit. It handles the case where
    the subreddit might not exist by printing "None".
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the top 10 hottest posts on a given subreddit.

    Args:subreddit (str): The name of the subreddit to query.Prints:
        The titles of the top 10 hottest posts. Prints "None" if the subreddit
        does not exist.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response and extract the 'data' section
    results = response.json().get("data")

    # Print the titles of the top 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]

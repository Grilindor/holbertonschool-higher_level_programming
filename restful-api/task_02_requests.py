#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""


import csv
import requests


def fetch_and_print_posts():
    """Fetching posts from JSONPlaceholder and printing titles"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetching posts from JSONPlaceholder and saving data to CSV"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.ok:
        posts = r.json()
        """Structuring data into a list of dictionaries"""
        data = [{'id': post['id'], 'title': post['title'],
                 'body': post['body']} for post in posts]

        with open('posts.csv', mode='w', newline='') as file:
            keys = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=keys)

            """Writing data to CSV with headers"""
            writer.writeheader()
            writer.writerows(data)

"""
Task 2: Consuming and processing data from an API using Python
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles."""
    # Send a GET request to the API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Print the status code
    print("Status Code:", response.status_code)

    # If the request was successful, parse and print titles
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to a CSV file."""
    # Send a GET request to the API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # If the request was successful, structure data and write to CSV
    if response.status_code == 200:
        posts = response.json()

        # Keep only id, title, and body for each post
        filtered_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write to CSV file
        with open("posts.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(filtered_posts)

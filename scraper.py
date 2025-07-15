import praw
import os
from dotenv import load_dotenv
import json

load_dotenv() 

def scrape_redditor_data(username: str, limit: int = 50):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    redditor = reddit.redditor(username)
    scraped_data = []

    # Scrape comments
    for comment in redditor.comments.new(limit=limit):
        scraped_data.append(f"Comment: {comment.body}")

    # Scrape posts 
    for submission in redditor.submissions.new(limit=limit):
        scraped_data.append(f"Post Title: {submission.title}\nPost Body: {submission.selftext}")

    return scraped_data

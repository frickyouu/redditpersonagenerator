import os
import praw
from dotenv import load_dotenv

print("Attempting to connect to Reddit")

try:
    load_dotenv()
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
        read_only=True,
    )

    # A simple check to see if the read-only instance is working
    # This will fetch the karma of a known public user.
    user = reddit.redditor("spez")
    print(f"Successfully fetched karma for user 'spez': {user.comment_karma}")
    print("Connection successful! Your credentials in the .env file are correct.")

except Exception as e:
    print(f"Connection failed. Error: {e}")
    print("This confirms the issue is with your credentials in the .env file.")
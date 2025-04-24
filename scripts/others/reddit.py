import praw
import os

# Retrieve credentials from environment variables
client_id = os.environ.get("REDDIT_CLIENT_ID")
client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
user_agent = "by u/RealNPC_"
username = "RealNPC_"
password = os.environ.get("REDDIT_PASSWORD")
subreddit_name = "test"
title = "Hello from PRAW using os.environ!"
selftext = "This is a test post created using PRAW and directly accessing environment variables."

if not all([client_id, client_secret, user_agent, username, password, subreddit_name]):
    print("Error: One or more Reddit API credentials or the subreddit name are not set as environment variables.")
else:
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password,
        )

        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title, selftext=selftext)
        print(f"Successfully created post: {submission.url}")
    except praw.exceptions.RedditAPIException as e:
        print(f"Error creating post: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

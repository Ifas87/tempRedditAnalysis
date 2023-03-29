import praw
import config

reddit = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent)

subreddit = reddit.subreddit('nosleep')

for submission in subreddit.top(limit=1):
    print(submission.selftext)


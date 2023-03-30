import praw
import config
from nrclex import NRCLex

reddit = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent)

bigString = ''
subreddit = reddit.subreddit('allthingsgucci')

for submission in subreddit.top(limit=100):
    bigString += submission.selftext

text_stuff = NRCLex(bigString)
results = text_stuff.raw_emotion_scores

print(results)


import praw
import config
from nrclex import NRCLex 

reddit = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent)

bigString = ''
subreddit = reddit.subreddit('LeopardsAteMyFace')

for submission in subreddit.top(limit=100):
    bigString += submission.title

text_stuff = NRCLex(bigString)
results = text_stuff.raw_emotion_scores

print(results)


def data_loading(subname, imageSubs=False):
    bigString = ''
    subreddit = reddit.subreddit(subname)

    if imageSubs:
        for submission in subreddit.top(limit=100):
            bigString += submission.title
    else:
        for submission in subreddit.top(limit=100):
            bigString += submission.selftext
    
    return bigString


def all_analysis(sampleString):
    text_stuff = NRCLex(bigString)
    results = text_stuff.raw_emotion_scores

    return results


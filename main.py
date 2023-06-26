import praw
import config
from nrclex import NRCLex
import sumy.summarizers.lex_rank as su
import sumy.parsers.plaintext as pt


reddit = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent)

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
    text_stuff = NRCLex(sampleString)
    results = text_stuff.raw_emotion_scores

    return results


if __name__ == "__main__":
    strs = data_loading(subname='pics', imageSubs=True)
    summariser = su.LexRankSummarizer(strs, 10)

    for sentence in summariser:
        print(sentence)
 
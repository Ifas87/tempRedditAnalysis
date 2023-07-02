import praw
import config
from nrclex import NRCLex
import sumy.summarizers.lex_rank as su
import sumy.parsers.plaintext as pt
import matplotlib.pyplot as plt
from wordcloud import WordCloud


reddit = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent)

def data_loading(subname, imageSubs=False, classe="1"):
    bigString = ''
    subreddit = reddit.subreddit(subname)

    if imageSubs:
        if classe == "1":
            for submission in subreddit.top(limit=100):
                bigString += submission.title
        elif classe == "2":
            for submission in subreddit.hot(limit=100):
                bigString += submission.title
        elif classe == "3":
            for submission in subreddit.new(limit=100):
                bigString += submission.title
    else:
        if classe == "1":
            for submission in subreddit.top(limit=100):
                bigString += submission.selftext
        elif classe == "2":
            for submission in subreddit.hot(limit=100):
                bigString += submission.selftext
        elif classe == "3":
            for submission in subreddit.new(limit=100):
                bigString += submission.selftext
    return bigString


def all_analysis(sampleString):  
    text_stuff = NRCLex(sampleString)
    results = text_stuff.raw_emotion_scores

    labels = list(results.keys())
    data = list(results.values())

    plt.figure(figsize=(10, 3))
    plt.bar(range(len(results)), data, tick_label=labels)
    plt.show()

    wordcloud = WordCloud().generate(sampleString)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    return results
 

if __name__ == "__main__":
    strs = all_analysis(data_loading(subname='pics', imageSubs=True))
    # summariser = su.LexRankSummarizer(strs, 10)

    # for sentence in summariser:
    #     print(sentence)
 
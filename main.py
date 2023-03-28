import praw
import config

reddit = praw.Reddit(client_id=config.client_id, client_secret=config.client_secret, user_agent=config.user_agent)

subreddit = reddit.subreddit('pics')



# print(subreddit.display_name)
# print(subreddit.title)
# print(subreddit.description)

# print(reddit.read_only)
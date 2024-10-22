import os
import tweepy
from datetime import datetime, timedelta

twitterAPIaccess = tweepy.Client(
                # bearer_token=os.environ.get('TWITTER_BEARER_TOKEN'),
                consumer_key=os.environ.get('TWITTER_API_KEY'), consumer_secret=os.environ.get('TWITTER_API_KEY_SECRET'),
                access_token=os.environ.get('TWITTER_ACCESS_TOKEN'), access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
                )

temp = twitterAPIaccess.search_all_tweets("hello world")
print(temp)
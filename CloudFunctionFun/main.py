import os
import json
from datetime import datetime, timezone, timedelta
import pandas as pd
import tweepy

def fetch_recent_tweets_for_user(client, user_id, start_time):
    # https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_users_tweets
    response = client.get_users_tweets(user_id, tweet_fields=["created_at"], 
        start_time=start_time)
    # print(type(response.data[0]))
    rows = []
    if response.data is not None:
        for tweet in response.data:
            # print(tweet.created_at)
            created_at = pd.Timestamp(tweet.created_at).strftime("%Y-%m-%d %H:%M:%S")
            values = {"tweet_id": tweet.id, "author_id": user_id, 
                "created_at": created_at, "text": tweet.text}
            rows.append(values)
    return rows

def entry_point(request): # flask.Request
    # ignore for now because there wont be any data in the
    # GET request
    token = os.environ.get("BEARER_TOKEN")
    # pip install tweepy
    client = tweepy.Client(bearer_token=token)

    user_id = 602989093 # @ZagMBB id fetched in previous video
    start_time = datetime.now(timezone.utc) - timedelta(days=30) # TODO: hours=24
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    tweet_rows = fetch_recent_tweets_for_user(client, user_id, start_time)
    print(tweet_rows) # look in the logs
    # TODO: insert tweet_rows to a big query table
    return "Success", 200


if __name__ == "__main__":
    entry_point(None)
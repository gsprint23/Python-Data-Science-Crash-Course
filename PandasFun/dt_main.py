from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import pandas as pd

tweet_ts_str = "2025-01-01 11:05:00"
tweet_ts_dt = datetime.strptime(tweet_ts_str, "%Y-%m-%d %H:%M:%S")
print(tweet_ts_dt, type(tweet_ts_dt))
print(tweet_ts_dt.month, tweet_ts_dt.hour)

now_dt = datetime.now()
print("current time:", now_dt)
time_since_tweet_td = now_dt - tweet_ts_dt
print(time_since_tweet_td.total_seconds())

tweet_ts_str2 = tweet_ts_dt.strftime("%B %d, %Y at %I:%M %p")
print(tweet_ts_str2)

tweet_ts_dt = tweet_ts_dt.replace(tzinfo=ZoneInfo("America/Los_Angeles"))
print(tweet_ts_dt)

# switching now to datetime functinality in pandas
# pd.Timestamp
df = pd.read_csv("tweets_2022-23.csv")
print(df.head())
df["created_at(UTC)"] = pd.to_datetime(df["created_at(UTC)"], utc=True)
print(df["created_at(UTC)"])

print(df["created_at(UTC)"].iloc[0], type(df["created_at(UTC)"].iloc[0]))
td = df["created_at(UTC)"].iloc[0] - df["created_at(UTC)"].iloc[1]
print(td, type(td))

df["hour"] = df["created_at(UTC)"].dt.hour
df["day_of_week"] = df["created_at(UTC)"].dt.day_name()
print(df.head())

afternoon_df = df[df["hour"] >= 12]
afternoon_df = df[df["created_at(UTC)"].dt.hour >= 12]
print(afternoon_df)

monday_df = df.groupby("day_of_week").get_group("Monday")
print(monday_df)

print(df["created_at(UTC)"].value_counts().sort_values())

df.set_index("created_at(UTC)", inplace=True)
print(df.index)

daily_counts_ser = df["text"].resample("D").count()
print(daily_counts_ser)
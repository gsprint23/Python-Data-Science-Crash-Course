import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import tweepy

url = "https://www.allmysportsteamssuck.com/ncaa-division-i-football-and-basketball-twitter-hashtags-and-handles/"

def scrape_team_twitter_info():
    response = requests.get(url)
    if response.status_code == 200: # OK
        # create a "soup" object from the response text
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)
        # find the rankingstable
        table = soup.find("table", attrs={"id": "rankingstable"})
        # print(table)
        # parse the header
        thead = table.find("thead")
        # print(thead)
        # grab all the column names from the header
        ths = thead.find_all("th")
        # print(ths)
        col_names = [th.get_text() for th in ths]
        print(col_names)
        # task: try to parse the tbody
        # a table (2D list) of all the rows in the body
        tbody = table.find("tbody")
        trs = tbody.find_all("tr")
        rows = []
        for tr in trs:
            row = []
            tds = tr.find_all("td")
            for td in tds:
                row.append(td.get_text())
            rows.append(row)
        # print(rows)
        df = pd.DataFrame(rows, columns=col_names)
        df = df.set_index("School")
        return df
    return None # TODO: should do better error handling

def fetch_user_account_info(client, username):
    # https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_user
    response = client.get_user(username=username, user_fields=["created_at", "description", "public_metrics"])
    print(type(response.data))
    user = response.data
    print(user.keys())
    values = {"user_id": user.id, "username": user.username, "created_at": user.created_at, "description": user.description}
    values.update(user.public_metrics)
    ser = pd.Series(values)
    return ser

if __name__ == "__main__":
    df = scrape_team_twitter_info()
    # print(df)
    print(df.loc["Gonzaga"])

    with open("twitter_keys.json") as infile:
        json_obj = json.load(infile)
        token = json_obj["bearer_token"]
        # pip install tweepy
        client = tweepy.Client(bearer_token=token)

    zag_username = df.loc["Gonzaga", "Men’s Basketball Team"][1:]
    print(zag_username)
    user_ser = fetch_user_account_info(client, zag_username)
    print(user_ser)
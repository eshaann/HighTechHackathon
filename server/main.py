import urllib.parse
import json
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/withhashtag/<hashtag>/<event>')
def getPostsWithHastag(hashtag, event):
    # if the hashtag parameter has multiple hashtags, they should be seperated by "-", i.e "BLM-LGBTQ-prochoice"
    # same thing with events


    keywordQuery = ""
    if (event != ""):
        while (event.find("-") >= 0):
            keywordQuery += event[0:(event.find("-"))] + " OR "
            event = event[(event.find("-")+1):(len(event))]
        keywordQuery += event

    hashtagQuery = ""
    if (hashtag != ""):
        while (hashtag.find("-") >= 0):
            keywordQuery += "#" + hashtag[0:(hashtag.find("-"))] + " OR "
            hashtag = hashtag[(hashtag.find("-")+1):(len(hashtag))]
        hashtagQuery += "#" + hashtag

    finalQuery = "(" + hashtagQuery + ") (" + keywordQuery + ")  place_country:US -is:retweet -is:reply has:links lang:en"

    query_params = {'query': finalQuery}
    return connect_to_endpoint(search_url, query_params)


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# Authentication helper method
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

if __name__ =='__main__':
    app.run()

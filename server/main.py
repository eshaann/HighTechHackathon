import urllib.parse
import json
import requests
from flask import Flask
from flask_cors import CORS


bearer_token = "AAAAAAAAAAAAAAAAAAAAAPFecwEAAAAAvjnPLEh2Fbw1XmDaJWY2xb6Hrt0%3D6c79gIlmb1Pz61b0f01jc0vTDLejrfkvUvAUm94pA5rACKXXxr"
search_url = "https://api.twitter.com/2/tweets/search/recent"
embed_url = "https://publish.twitter.com/oembed"

app = Flask(__name__)
CORS(app)

@app.route('/withhashtag/<hashtag>/<event>')
def getPostsWithHastag(hashtag, event):
    # if the hashtag parameter has multiple hashtags, they should be seperated by "-", i.e "BLM-LGBTQ-prochoice"
    # same thing with events

    # for testing purposes
    # event = "protest-rally-march"

    keywordQuery = ""
    if (event != ""):
        while (event.find("-") >= 0):
            keywordQuery += event[0:(event.find("-"))] + " OR "
            event = event[(event.find("-")+1):(len(event))]
        keywordQuery += event

    hashtagQuery = ""
    if (hashtag != ""):
        while (hashtag.find("-") >= 0):
            hashtagQuery += "#" + hashtag[0:(hashtag.find("-"))] + " OR "
            hashtag = hashtag[(hashtag.find("-")+1):(len(hashtag))]
        hashtagQuery += "#" + hashtag

    finalQuery = "(" + hashtagQuery + ") (" + keywordQuery + " -history) -is:retweet -is:reply lang:en has:media"

    query_params = {'query': finalQuery}
    obj = connect_to_endpoint(search_url, query_params)
    # return obj
    listOfIds = []

    responseList = obj["data"]

    test = ""
    for i in responseList:
        test += i["id"] + "-"

    return test[0:(len(test)-1)]


@app.route('/tweethtml/<usr>/<id>')
def getTweetHTML(usr, id):
    link = "https://twitter.com/" + usr + "/status/" + id
    params = {'url': link}
    json = connect_to_endpoint(embed_url, params)
    obj = json.loads(json)
    return obj["html"]

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

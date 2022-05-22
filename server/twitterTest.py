import urllib.parse
import requests
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAPFecwEAAAAAvjnPLEh2Fbw1XmDaJWY2xb6Hrt0%3D6c79gIlmb1Pz61b0f01jc0vTDLejrfkvUvAUm94pA5rACKXXxr"
search_url = "https://api.twitter.com/2/tweets/search/recent"

keywords = ["protest"]
keywordQuery = ""

for i in range(len(keywords) - 1):
    keywordQuery += keywords
    keywordQuery += "OR "
keywordQuery += "#" + keywords[len(keywords) - 1]

hashtags = ["BLM", "LGBTQ+"]
hashtagQuery = ""

for i in range(len(hashtags) - 1):
    hashtagQuery += "#" + hashtags[i]
    hashtagQuery += " OR "
hashtagQuery += "#" + hashtags[len(hashtags) - 1]

finalQuery = "(" + hashtagQuery + ")" + " (" + keywordQuery + ")"

query_params = {'query': finalQuery}

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)


if __name__ == "__main__":
    main()

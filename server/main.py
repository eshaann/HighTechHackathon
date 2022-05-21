import requests
from flask import Flask
app = Flask(__name__)

@app.route('/withhashtag/<hashtag>')
def getPostsWithHastag(hashtag):
    
    return 'The HashTag is: #' + hashtag

if __name__ =='__main__':
    app.run()

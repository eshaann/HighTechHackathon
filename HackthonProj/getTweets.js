function addEmbed(id) {
  bQ = document.createElement("blockquote")
  aTag = document.createElement("a")

  bQ.setAttribute("class", "twitter-tweet")
  bQ.setAttribute("id", id)

  // url = "https://twitter.com/" + usr + "/status/" + id
  url = "https://twitter.com/x/status/" + id

  aTag.setAttribute("href", url)

  toNest = document.getElementById("tweets")
  toNest.appendChild(bQ)

  addedBq = document.getElementById(id)
  addedBq.appendChild(aTag)
}

function httpGetAsync(url, func)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            func(xmlHttp.responseText);
    }
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function loadIds (ids) {
  listOfTweets = []

  while (ids.indexOf("-") >= 0) {
    id = ids.substring(0,ids.indexOf("-"))
    listOfTweets.push(id)
    ids = ids.substring(ids.indexOf("-")+1, ids.length)
  }
  listOfTweets.push(ids)

  for (i = 0; i < listOfTweets.length; i ++) {
    addEmbed(listOfTweets[i])
  }

  toNest = document.getElementById("tweets")
  scriptTag = document.createElement("script")
  scriptTag.setAttribute("async", "")
  scriptTag.setAttribute("src", "https://platform.twitter.com/widgets.js")
  scriptTag.setAttribute("charset", "utf-8")

  toNest.appendChild(scriptTag)

  // <script async="" src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
}

queryString = window.location.search;
urlParams = new URLSearchParams(queryString);

topics = urlParams.get("Hashtag_Choice")
console.log(topics)

httpGetAsync("http://127.0.0.1:5000/withhashtag/" + topics.substring(1, topics.length) + "/protest-rallies-rally-strike-protests-socialjustice-equality-people-today", loadIds)

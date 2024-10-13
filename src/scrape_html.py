import requests

def FetchAndSave(url, path):
    r =requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)


url = "https://animemangatoon.com/top-anime-and-k-drama-like-true-beauty/"


FetchAndSave(url, "data/webtoons.html")
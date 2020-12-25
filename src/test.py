import requests

BASE = "http://127.0.0.1:5000"

data = {"url": "https://www.youtube.com/watch?v=GMppyAPbLYk&t=318s"}
responsePost = requests.post(BASE + "/videos/2", data)
print(responsePost.json())

input()
responseGet = requests.get(BASE + "/videos/1")
print(responseGet.json())

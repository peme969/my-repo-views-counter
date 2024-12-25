import requests
repos = []
with requests.get("https://api.github.com/users/peme969/repos") as r:
    for d in r.json():
      repos.append(d['name'])

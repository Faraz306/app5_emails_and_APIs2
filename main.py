import requests

api_key = "629051b6c9ba4bd3b9f8f6fafcfaac6a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-11-06&sortBy=publishedAt&apiKey=629051b6c9ba4bd3b9f8f6fafcfaac6a"
request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
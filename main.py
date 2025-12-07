import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from send_email import send_email

api_key = "629051b6c9ba4bd3b9f8f6fafcfaac6a"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-12-06&sortBy=publishedAt&apiKey={api_key}"
response = requests.get(url)
content = response.json()

print("API Response:", content)

if content.get("status") == "ok" and content.get("articles"):
    body = ""
    for article in content["articles"]:
        title = article.get("title", "")
        description = article.get("description", "")
        if title and description:
            if article["title"] is not None:
                body = article["title"] + "\n" + article["description"] + "\n\n"
        body = body.encode("utf-8")
        send_email(message=body)
    print(body)
else:
    print("No articles found. Error:", content.get("message", "Unknown error"))
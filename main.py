import requests
from send_email import send_email


topic = "tesla"
api_key = "d7c9112300e84278a8748de393937687"
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

body = "Subject: Today's News\n\n"
request = requests.get(url)
content = request.json()

for article in content["articles"][:20]:
    body += str(article["title"]).capitalize() + "\n" + str(article["description"]) + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
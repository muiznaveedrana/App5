import requests
from send_email import send_email

api_key = "d7c9112300e84278a8748de393937687"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-13&sortBy=publishedAt&apiKey=d7c9112300e84278a8748de393937687"

body = ""
request = requests.get(url)
content = request.json()
for article in content["articles"]:
    body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(body)
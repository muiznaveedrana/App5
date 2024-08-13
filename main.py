import requests

api_key = "d7c9112300e84278a8748de393937687"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-13&sortBy=publishedAt&apiKey=d7c9112300e84278a8748de393937687"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    title = article[title]
    description = article["description"]
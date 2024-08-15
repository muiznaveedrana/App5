import requests
from send_email import send_email
import random
from datetime import datetime

def func():
    topics = ["tesla", "politics", "countries", "google", "apple", "samsung"]
    topic = random.choice(topics)  # Corrected random topic selection
    api_key = "your_api_key_here"  # Ideally, use environment variables for this

    # Using today's date dynamically
    today = datetime.today().strftime('%Y-%m-%d')
    url = f"https://newsapi.org/v2/everything?q={topic}&from={today}&sortBy=publishedAt&apiKey={api_key}&language=en"

    body = "Subject: Today's News\n\n"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        content = response.json()

        for article in content["articles"][:20]:
            body += str(article["title"]).capitalize() + "\n" + str(article["description"]) + "\n" + article["url"] + "\n\n"

        body = body.encode("utf-8")
        send_email(body)  # Call send_email without receiver

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

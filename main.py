import requests
from send_email import send_email
import random
from datetime import datetime, timedelta

def func():
    # Expanded list of topics
    topics = [
        "tesla", "politics", "countries", "google", "apple", "samsung",
        "technology", "sports", "health", "science", "entertainment", "business",
        "finance", "travel", "education", "climate", "world", "gaming"
    ]
    
    topic = random.choice(topics)  # Randomly choose a topic
    api_key = "d7c9112300e84278a8748de393937687"  # Ideally, use environment variables for this

    # Define date range (last 7 days)
    end_date = datetime.today()
    start_date = end_date - timedelta(days=7)

    # Format dates as strings
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    url = f"https://newsapi.org/v2/everything?q={topic}&from={start_date_str}&to={end_date_str}&sortBy=publishedAt&apiKey={api_key}&language=en"

    body = "Subject: Today's News\n\n"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        content = response.json()

        # Debugging: Print the URL and response
        print(f"API URL: {url}")
        print("API Response Content:", content)

        if content['totalResults'] > 0 and 'articles' in content:
            for article in content["articles"][:20]:
                title = article.get("title", "No title")
                description = article.get("description", "No description")
                url = article.get("url", "No URL")
                body += f"{title.capitalize()}\n{description}\n{url}\n\n"
        else:
            body += "No news articles found for this topic.\n\n"

        body = body.encode("utf-8")
        send_email(body)  # Ensure send_email function can handle this format

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

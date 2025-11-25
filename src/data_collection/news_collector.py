import requests
import pandas as pd
from datetime import datetime


class NewsCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/"

    def get_news(self, query, pages=1):
        """Получить новости по запросу"""
        articles = []
        for page in range(1, pages + 1):
            url = f"{self.base_url}everything?q={query}&apiKey={self.api_key}&page={page}"
            response = requests.get(url)
            data = response.json()
            articles.extend(data.get('articles', []))
        return articles


# Пример использования
if __name__ == "__main__":
    collector = NewsCollector("your_api_key")
    news = collector.get_news("Tesla", pages=2)
    print(f"Собрано {len(news)} новостей")
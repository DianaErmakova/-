# main.py
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_collection.news_collector import NewsCollector
from data_collection.stock_collector import StockCollector


def main():
    print("=== Запуск системы анализа рынка ===")

    # 1. Собираем новости
    news_collector = NewsCollector()
    news = news_collector.get_news("Tesla", pages=1)
    print(f"📰 Собрано {len(news)} новостей")

    # 2. Собираем данные по акциям
    stock_collector = StockCollector()
    stock_data = stock_collector.get_stock_data("TSLA")
    print(f"📈 Данные по акции: {stock_data['company_name']}")

    # 3. Здесь будет анализ и корреляция
    print("✅ Оба модуля работают!")


if __name__ == "__main__":
    main()
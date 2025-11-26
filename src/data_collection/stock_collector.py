import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


class StockCollector:
    def __init__(self):
        pass  # yfinance не требует API ключа!

    def get_stock_data(self, ticker, period="3mo"):
        """Получить данные по акции"""
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period)
            info = stock.info

            return {
                'ticker': ticker,
                'company_name': info.get('longName', ticker),
                'sector': info.get('sector', 'Unknown'),
                'history': hist,
                'current_price': hist['Close'].iloc[-1] if not hist.empty else None,
                'data_points': len(hist)
            }
        except Exception as e:
            print(f"Ошибка получения данных для {ticker}: {e}")
            return None

    def get_multiple_stocks(self, tickers, period="3mo"):
        """Получить данные по нескольким акциям"""
        results = {}
        for ticker in tickers:
            data = self.get_stock_data(ticker, period)
            if data:
                results[ticker] = data
        return results


# Пример использования
if __name__ == "__main__":
    collector = StockCollector()

    # Тестируем на одной акции
    tsla_data = collector.get_stock_data("TSLA")
    print(f"Данные Tesla: {tsla_data['data_points']} точек")

    # Или на нескольких
    stocks = collector.get_multiple_stocks(["TSLA", "AAPL", "NVDA"])
    print(f"Собрано данных по {len(stocks)} компаниям")
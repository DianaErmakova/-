import sys
import os

# Правильно добавляем путь к src
current_dir = os.path.dirname(__file__)  # папка tests
parent_dir = os.path.dirname(current_dir)  # папка diploma
src_path = os.path.join(parent_dir, 'src')

sys.path.insert(0, src_path)

try:
    from data_collection.stock_collector import StockCollector

    print("✅ Импорт успешен!")

    # Тестируем
    collector = StockCollector()
    data = collector.get_stock_data("TSLA")
    print(f"✅ Данные получены: {data['company_name']}")
    print(f"💰 Цена: ${data['current_price']:.2f}")

except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print(f"🔍 Ищем в: {src_path}")
    print(f"📁 Содержимое src: {os.listdir(src_path) if os.path.exists(src_path) else 'папка не найдена'}")
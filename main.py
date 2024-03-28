class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_price(self, item):
        return self.items.get(item)

    def update_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price


# Создаем несколько магазинов
store1 = Store("Магазин продуктов 'Овощи и Фрукты'", "ул. Пушкина, д. 10")
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store1.add_item("Молоко", 1.2)

store2 = Store("Магазин одежды 'Мода и Стиль'", "пр. Ленина, д. 20")
store2.add_item("Футболка", 15)
store2.add_item("Джинсы", 25)
store2.add_item("Куртка", 50)

store3 = Store("Магазин электроники 'Техносфера'", "ул. Гагарина, д. 5")
store3.add_item("Смартфон", 500)
store3.add_item("Ноутбук", 800)
store3.add_item("Планшет", 300)

# Тестируем методы магазина
print("Товары в магазине 'Овощи и Фрукты':", store1.items)
store1.update_price("Яблоки", 0.6)
print("Цена на яблоки обновлена:", store1.items)
store1.remove_item("Бананы")
print("Бананы удалены из ассортимента:", store1.items)
print("Цена на молоко:", store1.get_price("Молоко"))
